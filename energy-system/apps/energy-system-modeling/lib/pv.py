import pandas as pd
import pvlib
from dataclasses import dataclass


@dataclass(kw_only=True, frozen=True)
class Module:
    cellType: str
    v_mp: float
    i_mp: float
    v_oc: float
    i_sc: float
    alpha_sc: float
    beta_voc: float
    gamma_pmp: float
    cells_in_series: int
    temp_ref = 25
    surface_tilt: float
    azimuth: float


def poa_data_add_iam(
    df: pd.DataFrame,
    location: pvlib.location.Location,
    azimuth: float,
    surface_tilt: float,
):
    start_date = df.index.min()
    end_date = df.index.max()

    solar_pos = location.get_solarposition(
        times=pd.date_range(start_date, end_date, freq="h")
    )

    angle_of_incidence = pvlib.irradiance.aoi(
        solar_azimuth=solar_pos["azimuth"],
        solar_zenith=solar_pos["apparent_zenith"],
        surface_azimuth=azimuth,
        surface_tilt=surface_tilt,
    )

    incidence_angle_modifier = pvlib.iam.ashrae(aoi=angle_of_incidence)

    poa_fixed = (
        incidence_angle_modifier * df["poa_direct"]
        + df["poa_sky_diffuse"]
        + df["poa_ground_diffuse"]
    )

    return df.assign(
        aoi=angle_of_incidence,
        iam=incidence_angle_modifier,
        poa_global=poa_fixed,
    )


def cell_temp_poa(df: pd.DataFrame):
    return df.assign(
        temp_cell=pvlib.temperature.faiman(
            poa_global=df["poa_global"],
            temp_air=df["temp_air"],
            wind_speed=df["wind_speed"],  # type: ignore
        )
    )


def module_power_cec(m: Module, df: pd.DataFrame):
    I_L_ref, I_o_ref, R_s, R_sh_ref, a_ref, adjust = pvlib.ivtools.sdm.fit_cec_sam(
        celltype=m.cellType,
        v_mp=m.v_mp,
        i_mp=m.i_mp,
        v_oc=m.v_oc,
        i_sc=m.i_sc,
        alpha_sc=m.alpha_sc,
        beta_voc=m.beta_voc,
        gamma_pmp=m.gamma_pmp,
        cells_in_series=m.cells_in_series,
        temp_ref=m.temp_ref,
    )

    cec_params = pvlib.pvsystem.calcparams_cec(
        effective_irradiance=df["poa_global"],
        temp_cell=df["temp_cell"],
        I_L_ref=I_L_ref,
        I_o_ref=I_o_ref,
        alpha_sc=m.alpha_sc,
        a_ref=a_ref,
        R_sh_ref=R_sh_ref,
        R_s=R_s,
        Adjust=adjust,
    )

    return pvlib.pvsystem.max_power_point(*cec_params, method="newton")  # type: ignore
