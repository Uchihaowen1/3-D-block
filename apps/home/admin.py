from django.contrib import admin
from .models import loading, withdraw, notification

admin.site.register(loading)
admin.site.register(withdraw)
admin.site.register(notification)