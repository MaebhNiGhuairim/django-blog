from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)
    # list_display = ('title', 'updated_on')
    # search_fields = ['title', 'content']
    # prepopulated_fields = {'slug': ('title',)}