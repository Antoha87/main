# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField
from smart_selects.db_fields import ChainedForeignKey
from sorl.thumbnail import ImageField
from django_geoip.models import Country, Region, City


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=UserManager.normalize_email(email),
            username=username)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email,
                                password=password,
                                username=username)
        user.is_admin = True
        user.save(using=self._db)
        return user


class Client(AbstractBaseUser):
    email = models.EmailField(u'Email', max_length=255, unique=True, db_index=True)
    username = models.CharField(u'Пользователь',  max_length=255, unique=True)
    first_name = models.CharField(u'Имя',  max_length=255, blank=True)
    last_name = models.CharField(u'Фамилия',  max_length=255, blank=True)
    date_of_birth = models.DateField(u'День рождения',  blank=True, null=True)
    country = models.ForeignKey(Country, verbose_name=u'Страна', blank=True, null=True)
    region = ChainedForeignKey(Region, verbose_name=u'Регион', chained_field="country", chained_model_field="country", blank=True, null=True)
    city = ChainedForeignKey(City, verbose_name=u'Город', chained_field="region", chained_model_field="region", null=True, blank=True)
    phone_number = PhoneNumberField(u'Номер телефона', blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = u'Клиент'
        verbose_name_plural = u'Клиенты'

    @classmethod
    def get_client(cls, request):
        try:
            return Client.objects.get(user=request)
        except Exception:
            return

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name,)

    def get_short_name(self):
        return self.first_name

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
