# pylint: disable=no-member

import pandas as pd


def create_calendar(start="2019-01-01", end="2019-12-31"):
    start_ts = pd.to_datetime(start).date()

    end_ts = pd.to_datetime(end).date()

    # record timestamp is empty for now
    dates = pd.DataFrame(columns=["calendar"], index=pd.date_range(start_ts, end_ts))
    dates.index.name = "MC_Date"

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

    dates["MC_Day"] = dates.index.dayofweek.map(days_names.get)
    dates["MC_Week"] = pd.Int64Index(dates.index.isocalendar().week)
    dates["MC_Month"] = dates.index.month
    dates["MC_Quarter"] = dates.index.quarter
    dates["MC_Year_half"] = dates.index.month.map(lambda mth: 1 if mth < 7 else 2)
    dates["MC_Year"] = dates.index.year
    dates["MC_YearMonth"] = (
        dates["MC_Year"].astype(str) + "_" + dates["MC_Month"].astype(str)
    )
    dates.reset_index(inplace=True)
    dates.index.name = "MC_Date"

    return dates

