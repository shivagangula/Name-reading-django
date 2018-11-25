from django.db import connection

from user.Opreations.md5_encript import convertmd5
from user.models import user_singup_model

def signup_qurey(username,password,mobile_number,email):
    signup_details = [ username, password, mobile_number, email ]
    md5_hash = convertmd5(email)
    cursor = connection.cursor()
    query = """
                       SELECT md5_hash FROM user_user_singup_model
                       WHERE email= '{0}' AND password = '{1}';
                       """.format(email, password)
    cursor.execute(query)
    row = cursor.fetchall()

    try:

         if username == '':
                return {'info': 'Enter username '}

         if password == '':
             return {'info': 'Enter password '}
         if email == '':
             return {'info': 'Enter email '}
         if mobile_number == '':
             return {'info': 'Enter mobile number '}

         if "" in signup_details:
            return {'info': 'Enter all Detailes Properly'}

         if md5_hash in row[ 0 ]:
            return {'info': "user already exist"}

    except:
        md5_hash = convertmd5(email)
        user = user_singup_model(
            username=username,
            password=password,
            mobile_number=mobile_number,
            email=email,
            md5_hash=md5_hash
        )
        user.save()
        return {'info': 'success'}
