from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """ Custom Use Model """""

    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'

    GENDER_CHOICES = ((GENDER_MALE, 'Мужской'), (GENDER_FEMALE, 'Женский'))


    LANGUAGE_ENGLISH = 'en'
    LANGUAGE_RUSSIAN = 'ru'

    LANGUAGE_CHOICES = ((LANGUAGE_RUSSIAN, 'русский'), (LANGUAGE_ENGLISH, 'английский'))

    avatar = models.ImageField(null=True, blank=True)
    email = models.EmailField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, null=True, max_length=10, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, null = True, max_length=20, blank=True)
