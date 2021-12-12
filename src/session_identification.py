import re


def categorizeSession(session):
    # take the current session and categorize them based on multiple regex (only fullmatch)

    # 2000m row, 5000m row, 10000m row, etc.
    if bool(re.fullmatch(r"\d{,2}000m row", session)):
        return session, "Distance Row"
    # 8:21, 48:32, 10:02, etc.
    elif bool(re.fullmatch(r"\d{,3}:\d{,2} row", session)):
        return session, "Timed Row"
    # 2x500m/1:00r row, 2x1000m/0:30r row, etc.
    elif bool(re.fullmatch(r"\dx\d{,4}m/\d{,2}:\d{,2}r row", session)):
        return "Distance Interval Training", "Interval Training"
    # 3x4:00/1:00r row, etc.
    elif bool(re.fullmatch(r"\dx\d{,2}:\d{,2}/\d{,2}:\d{,2}r row", session)):
        return "Time Interval Training", "Interval Training"
    # v2000m/r...12 row, v2:00/r...11 row, etc.
    elif bool(re.fullmatch(r"v\d{,4}", session)):
        return "Variable Interval Training", "Interval Training"
    # well... None
    elif bool(re.fullmatch(r"None", session)):
        return "None", "None"
    # Anything not matching current regex (should not be the case normally)
    else:
        return "Other", "Other"
