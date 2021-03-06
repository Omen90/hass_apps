"""
Utility functions that are used everywhere inside Heaty.
"""

import datetime
import re
import time


# matches any character that is not allowed in Python variable names
INVALID_VAR_NAME_CHAR_PATTERN = re.compile(r"[^0-9A-Za-z_]")
# regexp pattern matching a range like 3-7 without spaces
RANGE_PATTERN = re.compile(r"^(\d+)\-(\d+)$")
# strftime-compatible format string for military time
TIME_FORMAT = "%H:%M"


def escape_var_name(name):
    """Converts the given string to a valid Python variable name.
    All unsupported characters are replaced by "_". If name would
    start with a digit, "_" is put infront."""

    name = INVALID_VAR_NAME_CHAR_PATTERN.sub("_", name)
    digits = tuple([str(i) for i in range(10)])
    if name.startswith(digits):
        name = "_" + name
    return name

def expand_range_string(range_string):
    """Expands strings of the form '1,2-4,9,11-12 to set(1,2,3,4,9,11,12).
    Any whitespace is ignored. If a float or int is given instead of a
    string, a set containing only that, converted to int, is returned."""

    if isinstance(range_string, (float, int)):
        return set([int(range_string)])

    numbers = set()
    for part in "".join(range_string.split()).split(","):
        match = RANGE_PATTERN.match(part)
        if match is not None:
            for i in range(int(match.group(1)), int(match.group(2)) + 1):
                numbers.add(i)
        else:
            numbers.add(int(part))
    return numbers

def build_date_from_constraint(constraint, default_date, direction=0):
    """Builds and returns a datetime.date object from the given constraint,
    taking missing values from the given default_date.
    In case the date is not valid (e.g. 2017-02-29), a ValueError is
    raised, unless a number has been given for direction, in which case
    the next/previous valid date will be chosen, depending on the sign
    of direction."""

    fields = {}
    for field in ("year", "month", "day"):
        fields[field] = constraint.get(field, getattr(default_date, field))

    while True:
        try:
            return datetime.date(**fields)
        except ValueError:
            if direction > 0:
                fields["day"] += 1
            elif direction < 0:
                fields["day"] -= 1
            else:
                raise

            # handle month/year transitions correctly
            if fields["day"] < 1:
                fields["day"] = 31
                fields["month"] -= 1
            elif fields["day"] > 31:
                fields["day"] = 1
                fields["month"] += 1
            if fields["month"] < 1:
                fields["month"] = 12
                fields["year"] -= 1
            elif fields["month"] > 12:
                fields["month"] = 1
                fields["year"] += 1

def format_time(when, format_str=TIME_FORMAT):
    """Returns a string representing the given datetime.time object.
    If no strftime-compatible format is provided, the default is used."""

    return when.strftime(format_str)

def parse_time_string(time_str, format_str=TIME_FORMAT):
    """Parses a string of the given strptime-compatible format
    into a datetime.time object. If the string has an invalid
    format, None is returned. If no format is provided, the default
    will be used."""

    # remove whitespace
    time_str = "".join(time_str.split())

    try:
        t_struct = time.strptime(time_str, format_str)
    except ValueError:
        return None

    return datetime.time(t_struct.tm_hour, t_struct.tm_min, t_struct.tm_sec)
