# sort-list
A [Sublime Text](http://www.sublimetext.com/) plugin that **automatically saves the current file after every modification**.

- [Synopsis](#synopsis)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Author](#author)

Synopsis
-------
In the occasion where you'd want Sublime Text to save the current file after
each change, you can use this plugin.

Demo
-------
![Image](https://github.com/jamesfzhang/auto-save/blob/master/demo.gif?raw=true)

Installation
-------
#### From Package Control
auto-save is available through [Sublime Package Control](https://sublime.wbond.net/packages/auto-save)
and is the recommended way to install.

#### From Github
Alternatively, you may install via GitHub by cloning this repository into the `Packages`
directory under Sublime Text's data directory:

On Mac:

```
cd ~/Library/Application Support/Sublime Text 3/Packages
git clone https://github.com/jamesfzhang/auto-save.git
```

## Usage
-------
**By default, auto-save is disabled** because it is a fairly invasive plugin. To make it less invasive, you can instruct it to only auto-save changes to the file that is active when you turn on auto-save. In this mode, it will ignore changes to all other files.

You can also instruct it to auto-backup the file instead of auto-saving it. The backup gets created in the same directory as its source file. The backup file takes the same name as its source file, with the string `.autosave` inserted directly before the file extension. When auto-save is disabled, the backup file is deleted.

There are two ways to enable it. You can press <kbd>Command + Shift + P</kbd> to bring up the Command Palette, and search for **AutoSave**. Here, there are 3 options:

- Toggle AutoSave: all files
- Toggle AutoSave: current file only
- Toggle AutoSave Backup: current file only

Alternatively, you can bind commands to turn the plugin on or off. For example, to toggle auto-save for all files, open "Preferences / Key Bindings - User" and add:

```json
{ "keys": ["shift+alt+super+o"], "command": "sort-list" }
```


## License
This code is licensed under the [MIT License](https://opensource.org/licenses/MIT).
