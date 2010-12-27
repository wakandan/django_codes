'''
Created on Dec 26, 2010

@author: akai
'''
from models import SearchKeyword
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
class SearchKeywordInline(admin.StackedInline):
    model = SearchKeyword
class FlatPageAdminWithKeywords(FlatPageAdmin):
    inlines = [SearchKeywordInline]


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdminWithKeywords)