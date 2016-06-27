# sort-list
A cross-language [Sublime Text](http://www.sublimetext.com/) plugin for sorting items in a list.

- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Tests](#usage)
- [Contributing](#contributing)
- [License](#license)


## Demo
![](https://raw.githubusercontent.com/kylebebak/questionnaire/master/examples/sort.gif)


## Installation

### From Package Control
`sort-list` is available via [Sublime Package Control](https://sublime.wbond.net/packages/sort-list). This is the recommended way to install the plugin.

### From Github
Alternatively, you may install via GitHub by cloning this repository into the `Packages`
directory under Sublime Text's data directory. For example, on OSX:

```
cd "~/Library/Application Support/Sublime Text 3/Packages"
git clone https://github.com/kylebebak/sort-list.git
```


## Usage
Highlight one or more lists and run the command. If the lists can't be sorted exceptions with line numbers will be displayed in the __quick panel__.

The name of the command is `sort_list`. It appears in the `Command Palette` as `SortList`. If you want to use it with a minimum of hassle add a shortcut to your `.sublime-keymap`.

```json
{ "keys": ["shift+alt+super+o"], "command": "sort_list" }
```


## Tests
From the root directory, run `python3 -m unittest discover --verbose`. Some of the tests will fail in Python 2, but the plugin still works fine in Sublime Text 2.


## Contributing
Fork it and create a pull request.

### Wish List
- reinsert leading and trailing whitespace, including new lines, after sorting the list
- allow for list delimeters with more than one character, e.g. `<%` and `%>`.


## License
This code is licensed under the [MIT License](https://opensource.org/licenses/MIT).
