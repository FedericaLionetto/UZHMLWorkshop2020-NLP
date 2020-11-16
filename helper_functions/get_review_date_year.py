def get_review_date_year(df_row):
    """
    Return the year of the review date.
    """
    review_date_year = None
    if (str(df_row['review_date_timestamp']) == 'NaT'):
        review_date_year = None
    else:
        review_date_year = df_row['review_date_timestamp'].year
    return review_date_year