from django.conf import settings
from django.db.models import CASCADE
from django.utils import timezone
from django.utils.text import slugify
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField
from taggit.managers import TaggableManager


# Create your models here.


class User(models.Model):
    user_level_id = models.CharField(max_length=255, default = '2')
    username = models.CharField(max_length=255, default = "", unique=True)
    password = models.CharField(max_length=20, default = "")
    first_name = models.CharField(max_length=255, default = "")
    last_name = models.CharField(max_length=255, default = "")
    email = models.EmailField(max_length=255, default = "")
    add1 = models.TextField(default = "")
    add2 = models.TextField(default = "")
    image = models.CharField(max_length=255, null = True)

    def __str__(self):
        return self.first_name


class Role(models.Model):
    role_type=models.ForeignKey(User,
                                related_name='users',on_delete=CASCADE)
    role_title = models.CharField(max_length=255, default = "")
    role_description = models.TextField(default = "")

    def __str__(self):
        return self.role_title


class Course(models.Model): #A course is made of one or more modules packed together.
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='courses_created', on_delete=CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    tags = TaggableManager()
    overview = models.TextField()
    info = models.CharField(max_length=10000)
    created = models.DateTimeField(default=timezone.now())
    thumbnail = models.FileField()

    class Meta:
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class RelatedCourse(models.Model):
    entryName = models.CharField(max_length=50)
    entryInfo = models.CharField(max_length=10000)
    time = models.DateTimeField(default=timezone.now())
    image = models.ImageField(upload_to='images', null=True, blank=True)
    relatedKey = models.ForeignKey(Course, on_delete=models.CASCADE)


class Module(models.Model): #A module is a single component, it can be a document, PDF, image, or Video you create and it can be distributed alone or as part of a course.
    course = models.ForeignKey(Course,
                               related_name='modules',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['course'])

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.order}, {self.title}"


class Content(models.Model):
    module = models.ForeignKey(Module,
                               related_name='contents',
                               on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE,
                                     limit_choices_to={'model__in':(
                                         'text', 'video',
                                         'image',
                                         'file')})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module'])

    class Meta:
        ordering = ['order']


class ItemBase(models.Model):
    owner = models.ForeignKey(User,
                              related_name='%(class)s_related',
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description=models.CharField(max_length=1000)
    tags = TaggableManager()
    created = models.DateTimeField(default=timezone.now())
    updated = models.DateTimeField(default=timezone.now())

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Text(ItemBase):
    content = models.TextField()


class File(ItemBase):
    file = models.FileField(upload_to='files')


class Image(ItemBase):
    file = models.FileField(upload_to='images')


class Video(ItemBase):
    url = models.URLField()
