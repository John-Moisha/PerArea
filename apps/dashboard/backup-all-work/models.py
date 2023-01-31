from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
# from apps.accounts.models import User


# default_photo = f'{settings.MEDIA_URL}default_template/TemplateAccord.pdf'
from .validators import *


def user_upload_passport1(instance, filename):
    path = f'{instance.id}/passport1/{filename}'
    return path


def user_upload_passport2(instance, filename):
    path = f'{instance.id}/passport2/{filename}'
    return path


def user_upload_transaction_doc(instance, filename):
    path = f'{instance.id}/transaction_doc/{filename}'
    return path


class Check(models.Model):
    user = models.OneToOneField('accounts.CustomUser', on_delete=models.CASCADE, related_name='money')
    # money
    balance = models.FloatField(default=0.00)
    debt = models.FloatField(default=0.00)


class Transaction(models.Model):
    user = models.OneToOneField('accounts.CustomUser', on_delete=models.CASCADE, related_name='trans')

    # Doc
    doc = models.FileField(null=True, default=None, blank=True, upload_to=user_upload_transaction_doc)


class Verification(models.Model):
    # user = models.ForeignKey('accounts.User', on_delete=models.PROTECT, null=False)
    user = models.OneToOneField('accounts.CustomUser', on_delete=models.CASCADE, related_name='verif')

    class SexChoices(models.TextChoices):
        Female = 'F', _('Женский')
        Male = 'M', _('Мужской')
        Unsure = 'U', _('сделайте свой выбор')

    # B-day & Sex
    date_of_birth = models.DateField(null=True)
    sex = models.CharField(
        max_length=1,
        choices=SexChoices.choices,
        default=SexChoices.Unsure,
        null=False,
    )

    # Location
    street_line = models.CharField(max_length=100)
    number = models.CharField(max_length=5)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=7)

    # Passports
    passport1 = models.FileField(null=True, default=None,
                                 upload_to=user_upload_passport1,
                                 validators=[validate_file_passport_size])
    passport2 = models.FileField(null=True, default=None,
                                 upload_to=user_upload_passport2,
                                 validators=[validate_file_passport_size])



