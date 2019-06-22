from django.contrib import admin
from .models import TestDafiti

class TestDafitiAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', )


admin.site.register(TestDafiti, TestDafitiAdmin)