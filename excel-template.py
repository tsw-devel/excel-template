#!/usr/bin/env python3
import os
import sys
import string
from argparse import ArgumentParser

import chardet
import pandas


def get_line_feed_code(path):
    with open(path, mode='rb') as f:
        rawdata = f.read()
        if b'\r\n' in rawdata:
            return '\r\n'
        else:
            return '\n'


def get_encoding(path):
    with open(path, mode='rb') as f:
        dat = chardet.detect(f.read())
    return dat['encoding']


def generate(excel_file_path, verbose=False):
    error_occur = False
    if not os.path.exists(excel_file_path):
        print('Not found {}'.format(excel_file_path))
        return 1

    file = pandas.ExcelFile(excel_file_path, encoding='utf-8')
    sheet_names = file.sheet_names
    for sheet_no, sheet_name in enumerate(sheet_names):
        sheet_dframe = file.parse(sheet_name, convert_float=True)

        if verbose:
            print('[{}]'.format(sheet_name))

        if ( not sheet_dframe.to_dict().keys() >= {'output', 'template'}):
            print("{} : Not found required keys('output', 'template')".format(sheet_name))
            continue

        for i, row in sheet_dframe.iterrows():
            if verbose:
                print('-' * 64)
                print(row)
            settings = row.to_dict()
            if ( not 'output' in settings):
                print("{} [{}]: Not found 'output' value".format(sheet_name, i + 1))
                error_occur = True
                continue
            if ( not 'template' in settings):
                print("{} [{}]: Not found 'template' value".format(sheet_name, i + 1))
                error_occur = True
                continue
            template_path = settings['template']
            outputfile_path = settings['output']

            try:
                encoding = get_encoding(template_path)
                line_feed_code = get_line_feed_code(template_path)
                with open(template_path, encoding=encoding) as fr:
                    tmpl = string.Template(fr.read())
                    gen = tmpl.safe_substitute(settings)
            except (OSError, TypeError):
                print("{} [{}]: Not found 'template' file".format(sheet_name, i + 1))
                error_occur = True
                continue

            try:
                with open(outputfile_path, mode='w', encoding=encoding, newline=line_feed_code) as fw:
                    fw.write(gen)
                    print ('generate OK > {}'.format(outputfile_path))
            except OSError:
                print ('generate NG (write failed) > {}'.format(outputfile_path))
                error_occur = True

    return 1 if error_occur else 0


def parse():
    desc = 'Simple template engine with Excel as data.'
    argparser = ArgumentParser(description=desc)
    argparser.add_argument('FILE', type=str,
                           help='test data excel file')
    argparser.add_argument('-v', '--verbose',
                           action='store_const',
                           const=True,
                           default=False,
                           help='print verbose message')
    args = argparser.parse_args()
    return args


if __name__ == '__main__':
    result = parse()
    sys.exit( generate(result.FILE, result.verbose) )
