import polars as pl
from enum import StrEnum


class DataJoinMethod(StrEnum):
    SUM = "SUM"
    MEAN = "MEAN"


def reset_start_to_zero(df: pl.DataFrame, cols: list[str]):
    mins_arr = [df[col].min() for col in cols]
    min_start = min(mins_arr)
    if not isinstance(min_start, int) and not isinstance(min_start, float):
        raise ValueError("min value should a float or a int")
    return df.with_columns([pl.col(col).sub(min_start) for col in cols])


def minly_to_hourly(
    df: pl.DataFrame,
    time_col: str,
    hourly_col="time_hourly",
    method: DataJoinMethod = DataJoinMethod.SUM,
):
    df_hourly = df.with_columns(
        [pl.col(time_col).mul(1 / 60).round().alias(hourly_col)]
    )
    df_hourly = df_hourly.drop(time_col)
    # if method == DataJoinMethod.MEAN:
    #     return df_hourly.group_by(hourly_col).mean()
    # else:
    return df_hourly.group_by(hourly_col).mean()


def minly_to_daily(
    df: pl.DataFrame,
    time_col: str,
    daily_col="time_daily",
    method: DataJoinMethod = DataJoinMethod.SUM,
):
    df_daily = df.with_columns(
        [pl.col(time_col).mul(1 / (60 * 24)).floor().alias(daily_col)]
    )
    df_daily = df_daily.drop(time_col)
    if method == DataJoinMethod.MEAN:
        return df_daily.group_by(daily_col).mean()
    else:
        return df_daily.group_by(daily_col).sum()


def add_min_cols(df: pl.DataFrame, cols: list[str], suffix="_min"):
    return df.with_columns(
        [pl.col(col).mul(1 / 60).round().alias(f"{col}{suffix}") for col in cols]
    )


def make_ts(
    df: pl.DataFrame,
    value_col,
    start_col="start_time_min",
    end_col="end_time_min",
) -> pl.DataFrame:
    """Creates a time series for a given data frame of tasks
    Works by adding values in the start time and subtracting them in the end_time col.

    Args:
        df (pl.DataFrame): Polars Data frame
        value_col (str): Column name of value column.
        start_col (str, optional): Column name of the tasks start time. Defaults to "start_time_min".
        end_col (str, optional): Column name of the tasks end time. Defaults to "end_time_min".

    Returns:
        (pl.DataFrame): a data frame with columns `time`, `diff`  and `diff_cum`
    """

    start_cum = df[[start_col, value_col]].group_by(start_col).sum()
    end_cum = df[[end_col, value_col]].group_by(end_col).sum()
    end_cum = end_cum.with_columns(pl.col(value_col).mul(-1.0).alias(value_col))

    res_df = start_cum.join(
        end_cum, left_on=start_col, right_on=end_col, how="outer_coalesce"
    )
    res_df = res_df.with_columns(
        pl.col(f"{value_col}_right").fill_null(strategy="zero"),
        pl.col(value_col).fill_null(strategy="zero"),
    )
    res_df = res_df.sort(start_col)
    res_df = res_df.with_columns(
        pl.col(value_col).add(pl.col(f"{value_col}_right")).alias("diff"),
    )

    res_df = res_df.with_columns(
        pl.col("diff").cum_sum().alias("diff_cum"),
    )

    res_df = res_df.rename({start_col: "time"})
    return res_df
