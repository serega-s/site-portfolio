from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Profile(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255)
    profile_pic = models.ImageField(blank=True, null=True, upload_to="images/", default='/user.png')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        name = str(self.first_name)
        if self.last_name:
            name += ' ' + str(self.last_name)
        return name

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    headline = models.CharField(max_length=255)
    sub_headline = models.CharField(max_length=255)
    body = RichTextUploadingField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    thumbnail = models.ImageField(blank=True, null=True, upload_to="", default="placeholder.jpg")
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.headline

    def save(self, *args, **kwargs):
        if self.slug == None:
            slug = slugify(self.headline)

            has_slug = Post.objects.filter(slug=slug).exists()
            count = 1

            while has_slug:
                count += 1
                slug = slugify(self.headline) + '-' + str(count)
                has_slug = Post.objects.filter(slug=slug).exists()

            self.slug = slug

        super().save(*args, **kwargs)

class PostComment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True, related_name='postcomments')
    body = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    @property
    def created_dynamic(self):
        now = timezone.now()
        return now
