def get_date_flown_day(df_row):
    """
    Return the day of the date flown.
    """
    date_flown_day = None
    if (str(df_row['date_flown_timestamp']) == 'NaT'):
        date_flown_day = None
    else:
        date_flown_day = df_row['date_flown_timestamp'].day
    return date_flown_day