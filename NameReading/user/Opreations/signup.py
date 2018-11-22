from user.Opreations.md5_encript import convertmd5
from user.models import user_singup_model


def signup_qurey(username,password,mobile_number,email):
    list1 = [username, password, mobile_number, email]
    email = email.lower()
    md5_hash = convertmd5(email)
    if " " in list1:
        return {'info': 'enter all detailes properly'}
    else:
        user = user_singup_model(
                        username,
                        password,
                   mobile_number,
                           email,
                         md5_hash
                                 )
        user.save()
        return {'info': 'registration success'}
