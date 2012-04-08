
from django.db import models

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, unique=True) 
    color_code = models.CharField(max_length=100, blank=True)
    category_order = models.IntegerField(null=True, blank=True)
    search_name = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = u'categories'

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<Category: %s>' % self

class Activity(models.Model):
    id = models.IntegerField(null=True, primary_key=True, blank=True)
    name = models.CharField(max_length=100, blank=True) 
    work = models.IntegerField(null=True, blank=True)
    activity_order = models.IntegerField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True)
    search_name = models.CharField(max_length=100, blank=True) 
    class Meta:
        db_table = u'activities'

    def __unicode__(self):
        if self.category:
            return u'%s@%s' % (self.name, self.category)
        else:
            return u'%s' % (self.name)

    def __repr__(self):
        return '<Activity: %s>' % self

            
class Tag(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, )
    autocomplete = models.BooleanField(blank=True)
    class Meta:
        db_table = u'tags'

    def __unicode__(self):
        return u'%s' % (self.name)

    def __repr__(self):
        return '<Tag: %s>' % self

class FactTag(models.Model):
    fact = models.ForeignKey('Fact')
    tag = models.ForeignKey('Tag')
    class Meta:
        db_table = u'fact_tags'
    

class Fact(models.Model):
    id = models.IntegerField(primary_key=True)
    activity = models.ForeignKey(Activity)
    start_time = models.DateTimeField() 
    end_time = models.DateTimeField(null=True, blank=True) 
    description = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, through='FactTag')
    class Meta:
        db_table = u'facts'

    @property
    def category(self):
        return self.activity.category

    @property
    def duration(self):
        try:
            duration = self.end_time - self.start_time
        except TypeError:
            raise ValueError('This task is not yet finished')
        return duration.total_seconds() / 3600

    def __unicode__(self):
        return '%s (%s%s)' % (self.activity, self.start_time,
                '' if not self.end_time else ' to %s' % self.end_time )

    def __repr__(self):
        return '<Fact: %s>' % self
