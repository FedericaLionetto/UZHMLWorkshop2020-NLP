def get_origin(df_row):
    """
    Return the origin of the flight.
    """
    origin = None
    if str(df_row['route'])=='nan':
        origin = None
    else:
        origin = df_row['route'].split(' to ')[0]
    return origin