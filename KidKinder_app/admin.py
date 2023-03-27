from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(About)
admin.site.register(Classes)
admin.site.register(Teachers)
admin.site.register(Parents)
admin.site.register(Gallery)
admin.site.register(Contact)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}