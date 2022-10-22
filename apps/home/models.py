from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class withdraw(models.Model):
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    acct_name    = models.CharField(max_length=100, verbose_name='Account Name')
    acct_number  = models.CharField(max_length=100, verbose_name='Account Number')
    bank_name    = models.CharField(max_length=100, verbose_name='Bank Name')
    amount       = models.CharField(max_length=100, verbose_name='Amount')
    email        = models.EmailField(max_length=100, verbose_name='Email')

    def __str__(self):
        return str(self.user)


class loading(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    wallet      = models.CharField(max_length=20)
    investment  = models.CharField(max_length=20)
    bonus       = models.CharField(max_length=20)
    deposit     = models.CharField(max_length=20)

    def __str__(self):
        return str(self.user)

class notification(models.Model):
  
    icons       = [
        ('fa fa-exclamation-triangle', 'failed'),
        ('fa fa-clock', 'pending'),
        ('fa fa-university', 'success'),
        ('fa fa-credit-card', 'withdraw'), 
        ('fa fa-envelope', 'info'),
    ]
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    time        = models.DateTimeField()
    title       = models.CharField(max_length=100)
    message     = models.CharField(max_length=100)
    icon        = models.CharField(max_length=30, choices=icons, default='info')

    def __str__(self):
        return str(self.user)

class aza(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    acc_name = models.CharField(max_length=100)
    acc_num = models.CharField(max_length=100)
    bank = models.CharField(max_length=100)
    ref = models.CharField(max_length=100, null=True, blank=True)
    code = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.user)
