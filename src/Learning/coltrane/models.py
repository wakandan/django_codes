from django.db import models
from django.contrib.auth.models import User
import datetime
from tagging.fields import TagField
from markdown import markdown

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=250, 
                             help_text='Maximum 250 characters.')
    slug = models.SlugField(unique=True,
                            help_text='Must be unique.')
    desc = models.TextField()
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['title']
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return "/categories/%s/" % self.slug
    
        

class Entry(models.Model):
    #constants for status column
    STATUS_LIVE = 1
    STATUS_DRAFT = 2
    STATUS_HIDDEN = 3
    STATUS_CHOICES = ((STATUS_LIVE,'Live'),
                      (STATUS_DRAFT,'Draft'),
                      (STATUS_HIDDEN,'Hidden'))
        
    title = models.CharField(max_length=250)
    excerpt = models.TextField(blank=True)
    body = models.TextField()
    
    #for optimizing purpose, html code will be generated only after 
    #user saves an entry into the database. Whenever he returns
    #to the page again, text will be presented
    excerpt_html = models.TextField(editable=False,
                                    blank=True)
    body_html = models.TextField(editable=False,
                                 blank=True)    
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    slug = models.SlugField(unique_for_date='pub_date')    
    
    #associate with a default user model
    author = models.ForeignKey(User,
                               default='default')
    is_commentable = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    
    #indicate if the entry should be displayed
    status = models.IntegerField(choices=STATUS_CHOICES,
                                 default=1)
    categories = models.ManyToManyField(Category)
    
    #for tagging application
    tags = TagField()
    
    
    class Meta:
        verbose_name_plural = 'Entries'
        ordering = ['-pub_date']
    def __unicode__(self):
        return self.title
    def save(self, force_insert=False,force_update=False):
        self.body_html = markdown(self.body)
        if self.excerpt:
            self.excerpt_html = markdown(self.excerpt)
        super(Entry,self).save(force_insert, force_update)
    def get_absolute_url(self):
        return "/coltrane/%s/%s/" % \
                (self.pub_date.strftime("%Y/%b/%d").lower(), 
                 self.slug)
