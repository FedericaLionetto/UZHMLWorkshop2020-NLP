def get_review_date_month(df_row):
    """
    Return the month of the review date.
    """
    review_date_month = None
    if (str(df_row['review_date_timestamp']) == 'NaT'):
        review_date_month = None
    else:
        review_date_month = df_row['review_date_timestamp'].month
    return review_date_month