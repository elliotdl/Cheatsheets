#IMPORT
import math   #math.sqrt(4)
import math as mt   #mt.sqrt(4)
from math import *   #sqrt(4)

# GITHUB
git add -A
git commit -m "asdf"
git push
git pull

# LOOP OVER FILES
import os
for file_as_str in os.listdir('C:/Python/'):
    if file_as_str.endswith('.csv'):

# PICKLE
import pickle
object = open('C:/Python/pickles/filename.pkl', 'wb') # write
pickle.dump( (x,y,z), object )
object.close()
import pickle
object = open('C:/Python/pickles/filename.pkl', 'rb') # read
x, y, z = pickle.load(object)
object.close()

# WORD
from docx import Document
document = Document('03APR17_O5 MALE.docx')     # read
document.save('new-file-name.docx')             # write

# CSV
import csv
df = pd.read_csv('file.csv', header=0/None, index_col=0/None)   # read
df.to_csv('file.csv')                                           # write

# EXCEL
df = pd.ExcelFile('file.xlsx').parse('Sheet1', header=0/None, index_col=0/None)     # read
pd.ExcelFile('file.xlsx').sheet_names
df.to_excel('file.xlsx')                                                            # write

# GITHUB NEW PROJECT
# create new_repo on github.com
# in terminal:
#   git init
#   git remote add origin https://github.com/elliotdl/new_repo.git
#   git pull origin master
# in windows: copy over pycharm .gitignore
# in terminal:
#   git add .
#   git commit -m "first commit"
#   git push origin