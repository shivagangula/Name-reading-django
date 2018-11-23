from django.db import connection

from user.Opreations.md5_encript import convertmd5


def SignInQuery(email, password):
    md5_hash = convertmd5(email)
    cursor = connection.cursor()
    list1 = [ email, password ]
    query = """
                    SELECT md5_hash FROM user_user_singup_model
                    WHERE email= '{0}' AND password = '{1}';
                    """.format(email, password)
    cursor.execute(query)
    row = cursor.fetchall()
    print(row)
    try:
          if email == "":
              return {'info':'enter email adress'}
          if password == "":
              return {'info':'enter password'}
          if "" in list1:
                return {'info': "type correctly"}
          if md5_hash in row[ 0 ]:
                return {'info': "success"}

    except:
          return {'info': "user is not there"}
