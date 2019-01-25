# excel-template
Simple template engine with Excel as data.  
Combine Excel data and template text.  
This software is released under the MIT License, see LICENSE file.

# How to use

1. Install dependent libraries.  
```sh
$ pip install -r requirements.txt
```

2. Prepare Excel data and template file.  
I prepared the following sample.  
* Template format: Jinja2  
  - template-settings-sample.j2.xlsx  
  - template/sample-template.S.j2
* Template format: Python Template strings  
  - template-settings-sample.xlsx  
  - template/sample-template.S

3. Run excel-template.  
```sh
$ python excel-template.py -j2 template-settings-sample.j2.xlsx 
Sheet sample-j2 data model : Found required keys('output', 'template')
generate OK > gen/add_test.S
generate OK > gen/sub_test.S
# For the Python Template Strings sample, it is below.
# python excel-template.py template-settings-sample.xlsx
```

The result file is output to the gen directory.

# About the format of Excel
The required data is as follows.
- output ... Output file path  
- template ... Template file path  

If the above does not exist, that sheet will be skipped.
The rule is just the above.  

# Attention

In the case of a record including blank data (in this case, id 4) as follows.

| id |  name   | height |
| -- | ------- | ------ |
|  1 |  Jack   |   180  |
|  2 |  Harry  |   185  |
|  3 |  Emily  |   160  |
|  4 |  Oliver |        |

Data (in this case, height) of a column containing blank data is handled as a float rather than an integer.  
That is, the ID1 data will be 180.0 instead of 180.

# About the format of template
The substitutions method follows Python Template strings and Jinja2.  

- [Python Template strings](https://docs.python.org/3/library/string.html#template-strings)
- [Jinja2](http://jinja.pocoo.org/)

