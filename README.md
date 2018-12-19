# excel-template
Simple template engine with Excel as data.  
Combine Excel data and template text.  
This software is released under the MIT License, see LICENSE file.

# How to use

1. Install dependent libraries.  
```sh
$ pip install chardet
$ pip install pandas
$ pip install xlrd
$ pip install jinja2
```

2. Prepare Excel data and template file.  
I prepared the following sample.  
* Template format: Python Template strings  
  - template-settings-sample.xlsx  
  - template/sample-template.S
* Template format: Jinja2  
  - template-settings-sample.j2.xlsx  
  - template/sample-template.S.j2

3. Run excel-template.  
```sh
$ python excel-template.py template-settings-sample.xlsx
generate OK > gen/add_test.S
generate OK > gen/sub_test.S
# For the jinja2 sample, it is below.
# python excel-template.py -j2 template-settings-sample.j2.xlsx

```

The result file is output to the gen directory.

# About the format of Excel
The required data is as follows.
- output ... Output file path  
- template ... Template file path  

The rule is just the above.  
All data can be substitution data.

# About the format of template
The substitutions method follows Python Template strings and Jinja2.  

- [Python Template strings](https://docs.python.org/3/library/string.html#template-strings)
- [Jinja2](http://jinja.pocoo.org/)

