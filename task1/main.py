import sys
import os
import xlrd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from laba_logging import *
InitLogFile()


InitFile(__file__)


class pair:
    def __init__(self, lesson, type, teacher, auditory):
        self.lesson = lesson
        self.type = type
        self.teacher = teacher
        self.auditory = auditory


class day:
    def __init__(self):
        self.pairs = {}
    def add_pair(self, num, lesson, type, teacher, auditory):
        self.pairs[num] = pair(lesson, type, teacher, auditory)

class schedule:
    def __init__(self, group, year, semester):
        self.group = group
        self.year = year
        self.semester = semester
        self.days = {}
    def add_day(self, week_day, day):
        self.days[week_day] = day
    


# Открытие файла
workbook = xlrd.open_workbook('файл.xls')
sheet = workbook.sheet_by_index(0)

# Чтение данных
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        print(f'[{row}][{col}] - {sheet.cell_value(row, col)}')

'''
# Для pandas
pip install pandas openpyxl xlrd

# Или только нужные компоненты
pip install pandas
pip install openpyxl  # для .xlsx файлов
pip install xlrd      # для старых .xls файлов
'''