from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from lessons.models import Lesson


@admin.register(Lesson)
class LessonAdmin(SummernoteModelAdmin):
    list_display = ('title', )
    search_fields = ('title', 'content', )
    summernote_fields = ('content', )
