# -*- coding: utf-8 -*-
# ITXConverter.py
# author: jamesj

from header.ITXConverter_h import *

# ----------------------------------------------------------------------------------------- #
# MAIN FUNCTION

# @fn main
# @brief INI To XSLX File Converter main function
if __name__ == '__main__':
# ----------------------------------------------------------------------------------------- #
# 1) Get Parameters
	iniPath = None
	xlsxPath = None
	sheetName = None

# 1-1) Check program mode
	xlsxPath, sheetName, iniPath = checkMode(sys.argv)

# ----------------------------------------------------------------------------------------- #
# 2) Check ini path
	checkIni(iniPath)
	checkXlsx(xlsxPath)

# ----------------------------------------------------------------------------------------- #
# 3) Load ini
	totalData = loadIni(iniPath)

# ----------------------------------------------------------------------------------------- #
# 4) Write xlsx
	writeXlsx(xlsxPath, sheetName, totalData)

