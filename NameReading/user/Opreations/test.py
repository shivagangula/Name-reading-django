from django.db import connection
from user.Opreations.md5_encript import convertmd5

row = [('kbkedcbkdjcbed',)]
md5_hash = 'kbkedcbkdjcbed'


if md5_hash == row[0][0]:
    print(row[0][0] + " and "+md5_hash)
else:
    print(row)