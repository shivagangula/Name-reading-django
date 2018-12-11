from django.db import models
from user.models import user_singup_model

class StringsTable(models.Model):
    user = models.ManyToManyField(user_singup_model)
    Strings = models.CharField(max_length=20)
    serched_date = models.DateTimeField()
    def __str__(self):
        return self.Strings