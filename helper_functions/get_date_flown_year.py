def get_date_flown_year(df_row):
    """
    Return the year of the date flown.
    """
    date_flown_year = None
    if (str(df_row['date_flown_timestamp']) == 'NaT'):
        date_flown_year = None
    else:
        date_flown_year = df_row['date_flown_timestamp'].year
    return date_flown_year