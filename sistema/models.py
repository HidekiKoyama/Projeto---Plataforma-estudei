from django.db import models


class categorie_curses(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=150)
    delete = models.BooleanField(default=True, blank=False)

    def __str__(self):
        return self.name


class courses(models.Model):
    user_log = models.ForeignKey(
        "auth.user", blank=True, null=True, on_delete=models.SET_NULL, default="")
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=155)
    categorie_course = models.IntegerField(null=False, blank=True, default="")
    delete = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.name


class friends(models.Model):
    friend_1 = models.IntegerField()
    friend_2 = models.IntegerField()
