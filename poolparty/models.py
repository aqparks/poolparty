from django.db import models


class Pool(models.Model):
    pool_name = models.CharField(max_length=250)
    pool_description = models.CharField(max_length=250)
    owner = models.CharField(max_length=100)
    contact_email = models.CharField(max_length=100)

    def __str__(self):
        return self.pool_name
