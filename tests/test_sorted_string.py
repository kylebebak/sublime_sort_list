import unittest
import json

from sorted_string import sorted_string


class TestSortedString(unittest.TestCase):
    SETTINGS_FILE_NAME = 'sort_list.sublime-settings'

    @classmethod
    def setUpClass(cls):
        with open(cls.SETTINGS_FILE_NAME) as settings_file:
            settings = json.load(settings_file)
        cls.slc, cls.elc = settings['start_list_chars'], settings['end_list_chars']
        # fix args for sorted string
        cls.sorted_string = lambda c, s: sorted_string(s, cls.slc, cls.elc)

    def test_list(self):
        self.assertEqual(self.sorted_string("['dog', 'cat', 'mouse']"),
                         "['cat', 'dog', 'mouse']")

    def test_tuple(self):
        self.assertEqual(self.sorted_string("('dog', 'cat', 'mouse')"),
                         "('cat', 'dog', 'mouse')")

    def test_trailing_comma(self):
        self.assertEqual(self.sorted_string("['dog', 'cat', 'mouse',]"),
                         "['cat', 'dog', 'mouse',]")

    def test_no_delimeters(self):
        self.assertEqual(self.sorted_string("'dog', 'cat', 'mouse'"),
                         "'cat', 'dog', 'mouse'")

    def test_whitespace(self):
        self.assertEqual(self.sorted_string("\n'dog',\n\n 'cat', 'mouse' \n"),
                         "'cat', 'dog', 'mouse'")

    def test_non_matching_delimeters(self):
        with self.assertRaises(SyntaxError) as cm:
            self.sorted_string("['dog', 'cat', 'mouse'")
            self.assertEqual("List delimeters don't match", str(cm.exception))
        with self.assertRaises(SyntaxError) as cm:
            self.sorted_string("['dog', 'cat', 'mouse')")
            self.assertEqual("List delimeters don't match", str(cm.exception))

    def test_not_parsable(self):
        with self.assertRaises(SyntaxError) as cm:
            self.sorted_string("'dog', 'cat', 'mous")
            self.assertEqual("List could not be parsed", str(cm.exception))

    def test_not_iterable(self):
        with self.assertRaises(SyntaxError) as cm:
            self.sorted_string("1")
            self.assertEqual("Not iterable", str(cm.exception))

    def test_unorderable(self):
        with self.assertRaises(TypeError) as cm:
            self.sorted_string("['dog', 2, 1]")
            self.assertEqual("The list contains unorderable types", str(cm.exception))


if __name__ == '__main__':
    unittest.main()
