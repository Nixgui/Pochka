import pymysql
from contextlib import closing
from pymysql.cursors import DictCursor
connection = pymysql.connect(
    host='',
    user='',
    password='',
    db='',
    charset='',
    cursorclass=DictCursor
)