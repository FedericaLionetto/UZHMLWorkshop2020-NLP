def get_review_date_day(df_row):
    """
    Return the day of the review date.
    """
    review_date_day = None
    if (str(df_row['review_date_timestamp']) == 'NaT'):
        review_date_day = None
    else:
        review_date_day = df_row['review_date_timestamp'].day
    return review_date_day