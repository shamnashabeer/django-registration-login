from django.db import models

# Create your models here.

class Contact(models.Model):
    contact_name=models.CharField(max_length=255)
    contact_email=models.EmailField(max_length=255)
    contact_msg=models.TextField(max_length=255)

    def __str__(self):
        return self.contact_name

class Registration(models.Model):
    registration_name=models.CharField(max_length=255)
    registration_email=models.CharField(max_length=255)
    registration_num=models.CharField(null=True,max_length=255)
    registration_use=models.CharField(null=True,max_length=255)
    registration_pass=models.CharField(null=True,max_length=255)

    def __str__(self):
        return self.registration_name