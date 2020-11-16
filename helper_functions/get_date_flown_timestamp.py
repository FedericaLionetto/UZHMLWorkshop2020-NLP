import datetime as dt
import dateutil

def get_date_flown_timestamp(df_row):
    """
    Return the timestamp of the date flown.
    """
    date_flown_timestamp = None
    if (str(df_row['date_flown']) == 'nan'):
        date_flown_timestamp = None
    elif (isinstance(df_row['date_flown'],dt.datetime)):
        date_flown_timestamp = df_row['date_flown']
    else:
        date_flown_timestamp = dateutil.parser.parse(df_row['date_flown'])
    return date_flown_timestamp