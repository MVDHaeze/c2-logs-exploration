""

import pandas as pd


def create_calendar(start, end):
    start_ts = pd.to_datetime(start).date()

    end_ts = pd.to_datetime(end).date()

    # record timestamp is empty for now
    dates = pd.DataFrame(columns=["calendar"], index=pd.date_range(start_ts, end_ts))
    dates.index.name = "Date"

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

    dates["Day"] = dates.index.dayofweek.map(days_names.get)
    dates["Week"] = pd.Int64Index(dates.index.isocalendar().week)
    dates["Month"] = dates.index.month
    dates["Quarter"] = dates.index.quarter
    dates["Year_half"] = dates.index.month.map(lambda mth: 1 if mth < 7 else 2)
    dates["Year"] = dates.index.year
    dates.reset_index(inplace=True)
    dates.index.name = "date_id"

    return dates
