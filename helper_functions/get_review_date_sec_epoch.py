def get_review_date_sec_epoch(df_row):
    """
    Return the seconds since the epoch of the review date.
    """
    review_date_sec_epoch = None
    if (str(df_row['review_date_timestamp']) == 'NaT'):
        review_date_sec_epoch = None
    else:
        review_date_sec_epoch = df_row['review_date_timestamp'].timestamp()
    return review_date_sec_epoch