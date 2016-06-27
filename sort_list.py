"""
SortList - Sublime Text Plugin

Sorts comma separated lists. Lists can span multiple lines. Can sort
multiple lists simultaneously via selection regions.

Prints exceptions to quick panel.
"""

import sublime, sublime_plugin

settings_filename = "sort_list.sublime-settings"


class SortListCommand(sublime_plugin.TextCommand):
    START_LIST_CHARS = "[{(<"
    END_LIST_CHARS = "]})>"

    def run(self, edit):
        settings = sublime.load_settings(settings_filename)
        slc = settings.get("start_list_chars") or self.START_LIST_CHARS
        elc = settings.get("end_list_chars") or self.END_LIST_CHARS

        view = self.view
        sel = view.sel()
        exceptions = []
        for region in sel: # handle multiple selection regions
            if not region.empty():
                try:
                    s = sorted_string(view.substr(region), slc, elc)
                except Exception as e: # include line number with exception
                    exceptions.append("{}: {}".format(
                        view.rowcol(region.begin())[0] + 1, str(e)
                    ))
                else:
                    view.replace(edit, region, s)
        if exceptions:
            self.show_quick_panel(exceptions, self.view.window())

    def show_quick_panel(self, messages, window):
        window.show_quick_panel(messages, None, sublime.MONOSPACE_FONT)


def sorted_string(s, start_list_chars, end_list_chars):
    """Accepts a string that represents a comma separated list of values.

    Parses the string to an iterable, sorts it, casts it back to a string
    and returns the string. Preserves the first and last chars of the string,
    assuming they are `list_chars`.

    Can also handle strings without opening and closing `list_chars`, and
    lists with a trailing comma.
    """
    # cache first and last chars in string, which may be list delimeters
    first, last = s[0], s[-1]
    if start_list_chars.find(first) != end_list_chars.find(last):
        raise SyntaxError("List delimeters don't match")

    trailing_comma = ',' if ',' in s[-2:] else ''
    if first in start_list_chars: # remove list delimeters from string
        s = s[1:-1]
    else: # string not bounded by list delimeters
        first, last = '', ''

    s = s.replace('\n', '').replace('\r', '') # for parsing multi-line lists
    try:
        l = eval(s)
    except:
        raise SyntaxError("List could not be parsed")
    if not hasattr(l, '__iter__'):
        raise SyntaxError("Not iterable")

    try:
        return first + str(sorted(l))[1:-1] + trailing_comma + last
    except TypeError:
        raise TypeError("The list contains unorderable types")
