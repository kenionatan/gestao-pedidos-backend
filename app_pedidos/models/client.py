from django.db import models


class Client(models.Model):
    client_name = models.CharField(max_length=200)

    def __str__(self):
        return self.client_name
