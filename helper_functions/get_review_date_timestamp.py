import dateutil

def get_review_date_timestamp(df_row):
    """
    Return the timestamp of the review date.
    """
    review_date_timestamp = None
    if (str(df_row['review_date']) == 'nan'):
        review_date_timestamp = None
    else:
        review_date_timestamp = dateutil.parser.parse(df_row['review_date'])
    return review_date_timestamp