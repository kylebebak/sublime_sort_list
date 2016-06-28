import json


def get_quote_char(s):
    sq, dq = "'", '"'
    sqi, dqi = s.find(sq), s.find(dq)
    if dqi is -1:
        return sq
    elif dqi is not -1 and sqi is -1:
        return dq
    else:
        return sq if sqi <= dqi else dq


def sorted_string(s, start_list_chars, end_list_chars):
    """Accepts a string that represents a comma separated list of values.

    Parses the string to an iterable, sorts it, casts it back to a string
    and returns the string. Preserves the first and last chars of the string,
    assuming they are `list_chars`.

    Handles strings without opening and closing `list_chars`, and lists with
    a trailing comma. Preserves the quote style (single quotes/double quotes)
    of the string.
    """
    s = s.strip().replace('\n', '').replace('\r', '') # for parsing multi-line lists
    sq, dq = "'", '"'
    quote_char = get_quote_char(s)

    # cache first and last chars in string, which may be list delimiters
    first, last = s[0], s[-1]
    if start_list_chars.find(first) != end_list_chars.find(last):
        raise SyntaxError("List delimiters don't match")

    if first in start_list_chars: # remove list delimiters from string
        s = s[1:-1]
    else: # string not bounded by list delimiters
        first, last = '', ''

    s = s.strip()
    trailing_comma = ''
    if s[-1] is ',':
        trailing_comma = ','
        s = s[:-1]

    try:
        l = json.loads('[' + s.replace(sq, dq) + ']') # `json.loads` chokes on single quotes
    except:
        raise ValueError("List could not be parsed")

    s = str(sorted(l))[1:-1]
    if quote_char is dq: # casting the list to a string wraps strings in single quotes
        s = s.replace(sq, dq)

    try:
        return first + s + trailing_comma + last
    except TypeError:
        raise TypeError("The list contains unorderable types")
