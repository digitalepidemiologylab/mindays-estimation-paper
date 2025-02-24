from datetime import datetime, timedelta


def process_string(
    s,
    ignore_vars=[
        "PDI_Quintile",
        "hPDI_Quintile",
        "HEI",
        "BMI",
    ],
    newLineSep=3,
):
    if s in ignore_vars:
        return s
    s = s.replace("_fg", "")
    # Step 1 & 2: Split the string by "_" and replace "_" with a space, then capitalize the first letter
    parts = s.replace("_eaten", "").split("_")
    # capitalized_parts = [part.capitalize() for part in parts]
    capitalized_parts = [part[0].upper() + part[1:] if part else "" for part in parts]

    # Step 3: If there are more than 3 items, insert "\n" in the middle
    if newLineSep and len(capitalized_parts) > newLineSep:
        mid_index = len(capitalized_parts) // 2
        processed_string = (
            " ".join(capitalized_parts[:mid_index])
            + "\n"
            + " ".join(capitalized_parts[mid_index:])
        )
    else:
        processed_string = " ".join(capitalized_parts)

    return processed_string


def remove_users_with_less_than_n_days(df, ndays=7):
    users_with_less_than_7days = (
        df["subject_key"].value_counts()[df["subject_key"].value_counts() < ndays].index
    )
    df = df[~df["subject_key"].isin(users_with_less_than_7days)]
    return df


def remove_days_with_less_than_n_kcal(df, kcal_threshold=1000):
    df = df.groupby(["subject_key", "eaten_day"]).filter(
        lambda x: x["energy_kcal_eaten"].sum() > kcal_threshold
    )
    return df


def longest_continuous_dates(dates):
    # Convert list of date strings to datetime objects
    date_objects = [datetime.strptime(date, "%Y-%m-%d") for date in dates]

    # Convert list to a set for O(1) look-up times
    date_set = set(date_objects)

    longest_streak = []

    for date in date_objects:
        # Check if this date is the start of a sequence
        if date - timedelta(days=1) not in date_set:
            current_date = date
            current_streak = [current_date]

            # Continue to the next date in the sequence
            while current_date + timedelta(days=1) in date_set:
                current_date += timedelta(days=1)
                current_streak.append(current_date)

            # Update the longest streak if the current streak is longer
            if len(current_streak) > len(longest_streak):
                longest_streak = current_streak

    # Convert the longest streak back to string format
    longest_streak_str = [date.strftime("%Y-%m-%d") for date in longest_streak]
    return longest_streak_str
