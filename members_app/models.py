from django.db import models

class Members(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(max_length=255)
    birth = models.DateField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)

    def __str__(self):
        return f'[{self.pk}] | {self.name} | {self.email}'

    def get_absolute_url(self):
        return f'/{self.pk}/'