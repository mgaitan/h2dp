# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Activities(models.Model):
    id = models.IntegerField(null=True, primary_key=True, blank=True)
    name = models.TextField(blank=True) # This field type is a guess.
    work = models.IntegerField(null=True, blank=True)
    activity_order = models.IntegerField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    category_id = models.IntegerField(null=True, blank=True)
    search_name = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'activities'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        db_table = u'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField()
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_group_permissions'

class AuthMessage(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    message = models.TextField()
    class Meta:
        db_table = u'auth_message'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)
    class Meta:
        db_table = u'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    is_superuser = models.BooleanField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = u'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = u'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_user_user_permissions'

class Categories(models.Model):
    id = models.IntegerField(null=True, primary_key=True, blank=True)
    name = models.TextField(blank=True) # This field type is a guess.
    color_code = models.TextField(blank=True) # This field type is a guess.
    category_order = models.IntegerField(null=True, blank=True)
    search_name = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'categories'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        db_table = u'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = u'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = u'django_site'

class FactIndex(models.Model):
    id = models.TextField(blank=True) # This field type is a guess.
    name = models.TextField(blank=True) # This field type is a guess.
    category = models.TextField(blank=True) # This field type is a guess.
    description = models.TextField(blank=True) # This field type is a guess.
    tag = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'fact_index'

class FactIndexContent(models.Model):
    docid = models.IntegerField(null=True, primary_key=True, blank=True)
    c0id = models.TextField(blank=True) # This field type is a guess.
    c1name = models.TextField(blank=True) # This field type is a guess.
    c2category = models.TextField(blank=True) # This field type is a guess.
    c3description = models.TextField(blank=True) # This field type is a guess.
    c4tag = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'fact_index_content'

class FactIndexSegdir(models.Model):
    level = models.IntegerField(null=True, primary_key=True, blank=True)
    idx = models.IntegerField(null=True, primary_key=True, blank=True)
    start_block = models.IntegerField(null=True, blank=True)
    leaves_end_block = models.IntegerField(null=True, blank=True)
    end_block = models.IntegerField(null=True, blank=True)
    root = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'fact_index_segdir'

class FactIndexSegments(models.Model):
    blockid = models.IntegerField(null=True, primary_key=True, blank=True)
    block = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'fact_index_segments'

class FactTags(models.Model):
    fact_id = models.IntegerField(null=True, blank=True)
    tag_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'fact_tags'

class Facts(models.Model):
    id = models.IntegerField(null=True, primary_key=True, blank=True)
    activity_id = models.IntegerField(null=True, blank=True)
    start_time = models.TextField(blank=True) # This field type is a guess.
    end_time = models.TextField(blank=True) # This field type is a guess.
    description = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'facts'

class Tags(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    autocomplete = models.BooleanField(null=True, blank=True)
    class Meta:
        db_table = u'tags'

class Version(models.Model):
    version = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'version'

