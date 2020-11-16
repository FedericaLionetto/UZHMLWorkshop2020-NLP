def get_date_flown_month(df_row):
    """
    Return the month of the date flown.
    """
    date_flown_month = None
    if (str(df_row['date_flown_timestamp']) == 'NaT'):
        date_flown_month = None
    else:
        date_flown_month = df_row['date_flown_timestamp'].month
    return date_flown_month