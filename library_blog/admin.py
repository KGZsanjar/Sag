from xml.dom.minidom import Comment
from django.contrib import admin

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','description','price','created_at','genre','author_gmail','author')
    list_filter = ('created_at','genre',)
    search_fields = ('title','description','author_gmail')


    admin.site.register(Genre)
    admin.site.register(Comment)
