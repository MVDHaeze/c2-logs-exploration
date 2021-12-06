# pylint: disable=no-member

import pandas as pd


def create_calendar(start="2019-01-01", end="2019-12-31"):
    start_ts = pd.to_datetime(start).date()

    end_ts = pd.to_datetime(end).date()

    # record timestamp is empty for now
    dates = pd.DataFrame(columns=["calendar"], index=pd.date_range(start_ts, end_ts))
    dates.index.name = "mc_date"

    days_names = {
        i: name
        for i, name in enumerate(
            [
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday",
            ]
        )
    }

    dates["mc_day"] = dates.index.dayofweek.map(days_names.get)
    dates["mc_week"] = pd.Int64Index(dates.index.isocalendar().week)
    dates["mc_month"] = dates.index.month
    dates["mc_quarter"] = dates.index.quarter
    dates["mc_year_half"] = dates.index.month.map(lambda mth: 1 if mth < 7 else 2)
    dates["mc_year"] = dates.index.year
    dates["mc_yearMonth"] = (
        dates["mc_year"].astype(str) + "_" + dates["mc_month"].astype(str)
    )
    dates.reset_index(inplace=True)
    dates.index.name = "mc_date"

    return dates

