# excel-template
Simple template engine with Excel as data.  
Combine Excel data and template text.  
This software is released under the MIT License, see LICENSE file.

# How to use

1. Install dependent libraries.  
```sh
pip install chardet
pip install pandas
pip install xlrd
```

2. Prepare Excel data and template file.  
I prepared the following sample.
  - template-settings-sample.xlsx  
  - template/sample-template.S


3. Run excel-template.  
```sh
python excel-template.py template-settings-sample.xlsx
```
The result file is output to the gen directory.

# About the format of Excel
The required data is as follows.
- output ... Output file path  
- template ... Template file path  

The rule is just the above.  
All data can be substitution data.

# About the format of template
The substitutions method follows python Template strings.
https://docs.python.org/3/library/string.html#template-strings
