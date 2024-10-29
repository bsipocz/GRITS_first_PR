import math


def angle_to_sexigesimal(angle_in_degrees, decimals=3):
    """
    Convert the given angle to a sexigesimal string of hours of RA.

    Parameters
    ----------
    angle_in_degrees : float
        A scalar angle, expressed in degrees

    Returns
    -------
    hms_str : str
        The sexigesimal string giving the hours, minutes, and seconds of RA for
        the given `angle_in_degrees`

    """
    if math.floor(decimals) != decimals:
        raise OSError('decimals should be an integer!')

    hours_num = angle_in_degrees*24/360
    hours = math.floor(hours_num)

    min_num = (hours_num - hours)*60
    minutes = math.floor(min_num)

    seconds = (min_num - minutes)*60

    #zero padding 
    format_string = '{:02}:{:02}:{:0'+str(2+1+decimals) + '.' + str(decimals) + 'f}'
    #print(format_string)
    return format_string.format(hours, minutes, seconds)
