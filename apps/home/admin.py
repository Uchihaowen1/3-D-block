from django.contrib import admin
from .models import aza, loading, withdraw, notification

admin.site.register(loading)
admin.site.register(withdraw)
admin.site.register(notification)
admin.site.register(aza)
