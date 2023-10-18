from django.contrib import admin
from .models import Note
class NotesAdmin(admin.ModelAdmin):
    list_display = ('note_title', 'pub_author', 'is_active')


admin.site.register(Note, NotesAdmin)
