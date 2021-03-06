# Generated by Django 3.2.3 on 2021-05-23 02:32

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Creation Date')),
                ('modification_date', models.DateField(auto_now=True, verbose_name='Modification Date')),
                ('elimination_date', models.DateField(auto_now=True, verbose_name='Elimination Date')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=120, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=200, verbose_name='Email')),
                ('description', models.TextField(verbose_name='Description')),
                ('reference_image', models.ImageField(blank=True, null=True, upload_to='authors/', verbose_name='Reference Image')),
                ('web', models.URLField(blank=True, null=True, verbose_name='Web')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('linkedin', models.URLField(blank=True, null=True, verbose_name='Linkedin')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Creation Date')),
                ('modification_date', models.DateField(auto_now=True, verbose_name='Modification Date')),
                ('elimination_date', models.DateField(auto_now=True, verbose_name='Elimination Date')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Category Name')),
                ('reference_image', models.ImageField(upload_to='categories', verbose_name='Reference Image')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Creation Date')),
                ('modification_date', models.DateField(auto_now=True, verbose_name='Modification Date')),
                ('elimination_date', models.DateField(auto_now=True, verbose_name='Elimination Date')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=150, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=200, verbose_name='Email')),
                ('subject', models.CharField(max_length=100, verbose_name='Subject')),
                ('message', models.TextField(verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Creation Date')),
                ('modification_date', models.DateField(auto_now=True, verbose_name='Modification Date')),
                ('elimination_date', models.DateField(auto_now=True, verbose_name='Elimination Date')),
                ('facebook', models.URLField(verbose_name='Facebook')),
                ('twitter', models.URLField(verbose_name='Twitter')),
                ('instagram', models.URLField(verbose_name='Instagram')),
                ('linkedin', models.URLField(verbose_name='Linkedin')),
            ],
            options={
                'verbose_name': 'Social Media',
                'verbose_name_plural': 'Social Media',
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Creation Date')),
                ('modification_date', models.DateField(auto_now=True, verbose_name='Modification Date')),
                ('elimination_date', models.DateField(auto_now=True, verbose_name='Elimination Date')),
                ('email', models.EmailField(max_length=200, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Subscriber',
                'verbose_name_plural': 'Subscribers',
            },
        ),
        migrations.CreateModel(
            name='Web',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Creation Date')),
                ('modification_date', models.DateField(auto_now=True, verbose_name='Modification Date')),
                ('elimination_date', models.DateField(auto_now=True, verbose_name='Elimination Date')),
                ('about', models.TextField(verbose_name='About')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone')),
                ('email', models.EmailField(max_length=200, verbose_name='Email')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
            ],
            options={
                'verbose_name': 'Web',
                'verbose_name_plural': 'Webs',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Creation Date')),
                ('modification_date', models.DateField(auto_now=True, verbose_name='Modification Date')),
                ('elimination_date', models.DateField(auto_now=True, verbose_name='Elimination Date')),
                ('title', models.CharField(max_length=150, unique=True, verbose_name='Post Title')),
                ('slug', models.CharField(max_length=150, unique=True, verbose_name='Slug')),
                ('description', models.TextField(verbose_name='Description')),
                ('contents', ckeditor.fields.RichTextField()),
                ('reference_image', models.ImageField(max_length=255, upload_to='images/', verbose_name='Reference Image')),
                ('published', models.BooleanField(default=False, verbose_name='Published / Not Published')),
                ('publication_date', models.DateField(verbose_name='Publication Date')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Creation Date')),
                ('modification_date', models.DateField(auto_now=True, verbose_name='Modification Date')),
                ('elimination_date', models.DateField(auto_now=True, verbose_name='Elimination Date')),
                ('author', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200, verbose_name='Email')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('approved_comment', models.BooleanField(default=False)),
                ('reference_image', models.ImageField(max_length=255, upload_to='images/', verbose_name='Reference Image')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post')),
            ],
        ),
    ]
