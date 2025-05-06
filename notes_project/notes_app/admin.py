from django.contrib import admin

from .models import Note

admin.site.site_header = "Brain Fart Admin"
admin.site.site_title = "Brain Fart Admin Area"
admin.site.index_title = "Welcome to the Brain Fart admin area"

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    
    
admin.site.register(Note, NoteAdmin)