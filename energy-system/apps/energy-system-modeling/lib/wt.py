from dataclasses import dataclass
from numpy.typing import ArrayLike
import numpy as np


@dataclass(kw_only=True, frozen=True)
class WindTurbine:
    cut_in_speed: float
    cut_out_speed: float
    rated_speed: float
    rated_power: float
    height: float
    efficiency: float


# source: https://www.mdpi.com/1996-1073/15/10/3579
def wind_change_height(ws_ref: ArrayLike, *, ref_height: float, hub_height: float):
    alpha = 1.0 / 7.0
    return np.array(ws_ref) * (hub_height / ref_height) ** alpha


# source: https://www.mdpi.com/1996-1073/15/10/3579
def wt_power(wind_speed: ArrayLike, t: WindTurbine):
    ws_np = np.array(wind_speed)
    power = np.zeros(len(ws_np))
    power[(ws_np < t.cut_in_speed) & (ws_np > t.cut_out_speed)] = 0
    power[(ws_np >= t.rated_speed) & (ws_np <= t.cut_out_speed)] = t.rated_power
    filter = (ws_np >= t.cut_in_speed) & (ws_np < t.cut_out_speed)
    power[filter] = t.efficiency * (
        (ws_np[filter] ** 3 - t.cut_in_speed**3)
        / (t.rated_speed**3 - t.cut_in_speed**3)
        * t.rated_power
    )
    return power
