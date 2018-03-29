import openpyxl as xl
import os
file_name = 'exam.xlsx'
path = 'D:\\Python\\workspace\\learning\\xls\\'
wb = xl.load_workbook(path+file_name)
ws = wb.active


if __name__ == "__main__":
    print (os.getcwd())
    os.chdir(path)
    print (os.getcwd())

