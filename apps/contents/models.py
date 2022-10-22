from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User


class homeContent(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    siteName        = models.CharField(max_length=50, null=True, blank=True)
    contentglobal   = models.CharField(max_length=250, null=True, blank=True)
    contentSuper    = models.CharField(max_length=250, null=True, blank=True)
    contentBasic    = models.CharField(max_length=250, null=True, blank=True)
    contentMini    = models.CharField(max_length=250, null=True, blank=True)
    contentglobal1   = models.CharField(max_length=250, null=True, blank=True)
    contentSuper1    = models.CharField(max_length=250, null=True, blank=True)
    contentBasic1    = models.CharField(max_length=250, null=True, blank=True)
    contentMini1    = models.CharField(max_length=250, null=True, blank=True)
    contentglobal2   = models.CharField(max_length=250, null=True, blank=True)
    contentSuper2    = models.CharField(max_length=250, null=True, blank=True)
    contentBasic2    = models.CharField(max_length=250, null=True, blank=True)
    contentMini2    = models.CharField(max_length=250, null=True, blank=True)
    contentglobal3   = models.CharField(max_length=250, null=True, blank=True)
    contentSuper3    = models.CharField(max_length=250, null=True, blank=True)
    contentBasic3    = models.CharField(max_length=250, null=True, blank=True)
    contentMini3    = models.CharField(max_length=250, null=True, blank=True)
    contentglobal4   = models.CharField(max_length=250, null=True, blank=True)
    contentSuper4    = models.CharField(max_length=250, null=True, blank=True)
    contentBasic4    = models.CharField(max_length=250, null=True, blank=True)
    contentMini4    = models.CharField(max_length=250, null=True, blank=True)
    contentglobal5   = models.CharField(max_length=250, null=True, blank=True)
    contentSuper5    = models.CharField(max_length=250, null=True, blank=True)
    contentBasic5    = models.CharField(max_length=250, null=True, blank=True)
    contentMini5    = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.user

    class Meta:
        db_table = 'homeContent'
        verbose_name = 'Home Content'
        verbose_name_plural = 'Home Contents'
        