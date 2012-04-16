import peewee
from settings import DB_PATH

hamster_db  = peewee.SqliteDatabase(DB_PATH)

class Category(peewee.Model):
    id = peewee.PrimaryKeyField()
    name = peewee.CharField() 
    color_code = peewee.TextField(blank=True) # This field type is a guess.
    category_order = peewee.IntegerField(null=True, blank=True)
    search_name = peewee.TextField(blank=True) # This field type is a guess.
    class Meta:
        database = hamster_db
        db_table = u'categories'

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<Category: %s>' % self

class Activity(peewee.Model):
    id = peewee.PrimaryKeyField()
    name = peewee.CharField() 
    work = peewee.IntegerField(null=True, blank=True)
    activity_order = peewee.IntegerField(null=True, blank=True)
    deleted = peewee.IntegerField(null=True, blank=True)
    category = peewee.ForeignKeyField(Category)
    search_name = peewee.TextField(blank=True) # This field type is a guess.
    class Meta:
        database = hamster_db
        db_table = u'activities'

    def __unicode__(self):
        if self.category:
            return u'%s@%s' % (self.name, self.category)
        else:
            return u'%s' % (self.name)

    def __repr__(self):
        return '<Activity: %s>' % self

class Fact(peewee.Model):
    id = peewee.PrimaryKeyField()
    activity = peewee.ForeignKeyField(Activity)
    start_time = peewee.DateTimeField()
    end_time = peewee.DateTimeField()
    description = peewee.TextField(blank=True) 
    class Meta:
        database = hamster_db
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


class Tag(peewee.Model):
    id = peewee.PrimaryKeyField()
    name = peewee.TextField()
    autocomplete = peewee.BooleanField(null=True, blank=True)
    class Meta:
        database = hamster_db
        db_table = u'tags'

    def __unicode__(self):
        return u'%s' % (self.name)

    def __repr__(self):
        return '<Tag: %s>' % self

class FactTag(peewee.Model):
    fact = peewee.ForeignKeyField(Fact)
    tag = peewee.ForeignKeyField(Tag)
    class Meta:
        database = hamster_db
        db_table = u'fact_tags'
