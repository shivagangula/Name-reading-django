from django.db import connection

from user.Opreations.signin import pk
from user.models import user_singup_model
from user_profile.models import StringsTable


def pro_query(md5_hash):
    pkva= pk[0]

    get_strings = StringsTable.objects.filter(user = pkva).values_list("Strings"
                                                              ,"serched_date")
    list_of_strings = get_strings
    get_user = user_singup_model.objects.filter(pk = pkva).values_list("username",
                                                                      "mobile_number",
                                                                      "email")
    print(get_user)
    return {'strings': list_of_strings,'user_detailes':get_user}
