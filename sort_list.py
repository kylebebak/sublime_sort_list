"""
SortList - Sublime Text Plugin

Sorts comma separated lists. Lists can span multiple lines. Can sort
multiple lists simultaneously via selection regions.

Prints exceptions to quick panel.
"""

import sublime, sublime_plugin

from .sorted_string import sorted_string

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
