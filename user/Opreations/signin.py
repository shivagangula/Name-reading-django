from django.db import connection
from user.Opreations.md5_encript import convertmd5

md5_for_profile = []
pk = [ ]
def pkm(md5):
    i = md5
    cursor = connection.cursor()
    query = """select * from user_user_singup_model 
                     where md5_hash = "{}";""".format(i)
    cursor.execute(query)
    row = cursor.fetchall()
    user_serial_id = row[ 0 ][ 0 ]
    pk.append(user_serial_id)


def currentUser(email):
    md5_hash = convertmd5(email)
    cursor = connection.cursor()
    query = """
                        select username from user_user_singup_model 
                         where email = '{0}' ;
                        """.format(email)
    cursor.execute(query)
    row = cursor.fetchall()
    return row[0][0]

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
    cuser = currentUser(email)

    try:
          if email == "":
              return {'info':'enter email adress'}
          if password == "":
              return {'info':'enter password'}
          if "" in list1:
                return {'info': "type correctly"}
          if md5_hash in row[ 0 ]:
                md5_for_profile.append(md5_hash)
                pkm(md5_hash)
                return {'info': "success", 'username': cuser}


    except:
          return {'info': "user is not there"}

