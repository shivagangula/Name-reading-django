from django.db import connection

from user.Opreations.md5_encript import convertmd5


def signin_qurey(email,password):
    email = email.lower()
    md5_hash = convertmd5(email)
    cursor = connection.cursor()
    query = """ 
                 SELECT md5_hash FROM user_user_singup_model
                    WHERE email= '{0}' AND password = '{1}';
                    """.format(email, password)
    cursor.execute(query)
    row = cursor.fetchall()

    if md5_hash in row[0]:
       return  {'info': "user is there"}
    else:
        return {'info': "user is not there"}
