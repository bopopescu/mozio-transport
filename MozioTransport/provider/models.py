from django.db import models
from django.core.validators import RegexValidator
from djmoney.models.fields import MoneyField
from languages.fields import LanguageField


class Provider(models.Model):
    name = models.CharField(max_length=255, blank=True, default='')
    email = models.EmailField(max_length=255,blank=True,)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Please use this format '+999999999' with 15 digits max.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    language = LanguageField()
    currency = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created_at',)
        verbose_name_plural = 'providers'
