from django.db import models


class AccountModel(models.Model):
    user = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)

    def __str__(self):
        return self.user

    class Meta:
        db_table = 'user_details'
    
