def get_layover(df_row):
    """
    Return the layover of the flight.
    """
    layover = None
    if str(df_row['route'])=='nan':
        layover = None
    else:
        # print(df_row['route'])
        temp = df_row['route'].split(' via ')
        # There is no ' via ' in the route, no layover.
        if len(temp) == 1:
            layover = 'NA'
        # There is a ' via ' in the route, layover available.
        elif len(temp) == 2:
            layover = temp[1]
        else:
            layover = None
    return layover