from django.db import models
import datetime

class GitPull(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=50)


class SSHauth(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=50)
    server_ip=models.CharField(max_length=13)   
    posting_date = models.DateTimeField(auto_now_add=True)
