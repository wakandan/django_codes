'''
Created on Dec 26, 2010

@author: akai
'''
from django.contrib import admin
from models import Category, Entry

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['title']}
    pass

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['title']}
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)