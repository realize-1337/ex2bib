# Project Title

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

With this script you can use excel to effectively manage your glossaries with excel instead of writing them by hand.


## Usage <a name = "usage"></a>

One entry in the .bib file will look like this:<br>

```
@abbreviation{HTML,
short = {HTML},
long = {hypertext markup language}
}
```


### Excel setup
First of all, each Excel sheet represents one .bib file.
Therefore one can create multiple .bib files at once. <br><br>

![Excel Screenshot](https://i.imgur.com/29rtI7y.png)

The first column defines the type of the entry, e.g. 'symbol' or 'abbreviation'.<br>
The second column gives it it's index, which is the name used to access it within LaTeX<br><br>

Every following argument will be inserted in the entry with `%COLUMNNAME% = {%ARGUMENT%}`.<br>

If the cell in Excel starts with '$$' the `%ARGUMENT%` will be inserted as `\ensuremath{%ARGUMENT%}`<br>
If the cell in Excel starts with '_si_' the `%ARGUMENT%` will be inserted as `\si{%ARGUMENT%}`<br>


### Usage of the script

To run the script first install the requirements `pip install -r .\requirements.txt`<br>

Afterwards the script can be run with `python .\ex2bib.py %FILENAME%.xlsx`.<br>
With `python .\ex2bib.py --help` you will return
```
Run the programm with "python .\ex2bib.py %ARGUMENTS%
The following arguments are available:
--help -> shows this help (alternative: --h or --options)

Regular usage:
First argumement: Excel-Filename as "%FILENAME%.xlsx"
Second argument (optional): output path, e.g., "outputFolder" or "examples"; default = root
Third argument (optional): Mode "--overwrite" or "--append"; default = --overwrite

--overwrite (default): overwrites old .bib file
--append: appends entries to the existing .bib file.

Note: If .bib files do not exist they will be created automatically. 
```