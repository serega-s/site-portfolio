# Generated by Django 3.2.5 on 2021-07-18 09:01

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('sub_headline', models.CharField(max_length=255)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
                ('thumbnail', models.ImageField(blank=True, default='images/placeholder.jpg', null=True, upload_to='images/')),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(max_length=255)),
                ('profile_pic', models.ImageField(blank=True, default='/user.png', null=True, upload_to='images/')),
                ('bio', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.profile')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='base.Tag'),
        ),
    ]
