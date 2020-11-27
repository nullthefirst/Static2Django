from django.contrib import admin

from .models import FunFactSubmission


class FunFactSubmissionAdmin(admin.ModelAdmin):
    fields = ['username', 'fun_fact']


admin.site.register(FunFactSubmission, FunFactSubmissionAdmin)
