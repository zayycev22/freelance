from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=32)
    text = models.CharField(max_length=250)
    cost = models.FloatField()
    name = models.CharField(max_length=32)
    status = models.CharField(max_length=16)
    type = models.CharField(max_length=16)
    date = models.DateField()
    submit_user_id = models.IntegerField(default=0)
    create_user_id = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    #user_id = models.IntegerField(default=0)


class UserInfo(models.Model):
    text = models.CharField(max_length=250)
    userid = models.IntegerField()


# types:
# design,
# backend,
# frontend,
# brain.
