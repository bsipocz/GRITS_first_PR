import math

def angle_to_sexagesimal(angle_in_degrees, decimals=3):
    """
    Convert the given angle to a sexagesimal string of hours of RA.

    Parameters
    ----------
    angle_in_degrees : float
        A scalar angle, expressed in degrees
    decimals : int, optional
        Number of decimal places for the seconds, default is 3.

    Returns
    -------
    hms_str : str
        The sexagesimal string giving the hours, minutes, and seconds of RA for
        the given `angle_in_degrees`

    """
    if not isinstance(decimals, int) or decimals < 0:
        raise ValueError('decimals should be a non-negative integer!')

    # Correct conversion factor: 15 degrees per hour
    hours_num = angle_in_degrees / 15
    hours = int(hours_num)

    min_num = (hours_num - hours) * 60
    minutes = int(min_num)

    seconds = (min_num - minutes) * 60

    # Format with two-digit minutes and seconds and user-specified decimal places
    format_string = f'{hours}:{minutes:02}:{seconds:0{2 + decimals + 1}.{decimals}f}'
    return format_string

# Example usage:
# angle_to_sexagesimal(45) should return something like "3:00:00.000"

