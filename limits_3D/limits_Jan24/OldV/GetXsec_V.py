#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5

import sys, xlrd


if __name__ == '__main__' :
    Index_name=range(29)
    excel = xlrd.open_workbook('/Users/zhixingwang/Dropbox/DM_Xsec_50GeVstep_V&AV_removed.xlsx')
    Line=int(sys.argv[1])
    print(excel.sheet_by_name('DM_V').cell(Line,9).value)
