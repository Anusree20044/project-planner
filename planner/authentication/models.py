from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class RoleChoices(models.TextChoices):

    USER = "developer","developer"
    ADMIN = "admin","admin"

    PROJECT_COORDINATOR = 'project coordinator','project coordinator'

class Techchoices(models.TextChoices):

    FRONTEND = 'Frontend Developer','Frontend Developer'

    BACKEND = 'Backend Developer','Backend Developer'

    FULLSTACK = 'Fullstack Developer','Fullstack Developer'

    UIUX = 'UI/UX Designer','UI/UX Designer'

    TESTER = 'Software Tester','Software Tester'

class Profile(AbstractUser):

    role = models.CharField(max_length=20, choices=RoleChoices.choices)

    tech = models.CharField(max_length=20,choices = Techchoices.choices,null=True,blank=True)

    def __str__(self):

        return self.username

    class Meta:

        verbose_name = "profile"

        verbose_name_plural = "profiles"

    def __str__(self):

        return f"{self.username} - {self.role} - {self.tech}"


