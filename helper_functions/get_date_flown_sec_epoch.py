def get_date_flown_sec_epoch(df_row):
    """
    Return the seconds since the epoch of the date flown.
    """
    date_flown_sec_epoch = None
    if (str(df_row['date_flown_timestamp']) == 'NaT'):
        date_flown_sec_epoch = None
    else:
        date_flown_sec_epoch = df_row['date_flown_timestamp'].timestamp()
    return date_flown_sec_epoch