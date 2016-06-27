def sorted_string(s, start_list_chars, end_list_chars):
    """Accepts a string that represents a comma separated list of values.

    Parses the string to an iterable, sorts it, casts it back to a string
    and returns the string. Preserves the first and last chars of the string,
    assuming they are `list_chars`.

    Can also handle strings without opening and closing `list_chars`, and
    lists with a trailing comma.
    """
    s = s.strip().replace('\n', '').replace('\r', '') # for parsing multi-line lists

    # cache first and last chars in string, which may be list delimeters
    first, last = s[0], s[-1]
    if start_list_chars.find(first) != end_list_chars.find(last):
        raise SyntaxError("List delimeters don't match")

    if first in start_list_chars: # remove list delimeters from string
        s = s[1:-1]
    else: # string not bounded by list delimeters
        first, last = '', ''
    s = s.strip()
    trailing_comma = ',' if ',' is s[-1] else ''

    try:
        l = eval(s)
    except:
        raise ValueError("List could not be parsed")
    if not hasattr(l, '__iter__'):
        raise SyntaxError("Not iterable")

    try:
        return first + str(sorted(l))[1:-1] + trailing_comma + last
    except TypeError:
        raise TypeError("The list contains unorderable types")
