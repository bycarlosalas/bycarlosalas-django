
from django.db import models
from ckeditor.fields import RichTextField

class ModelBase(models.Model):
    id = models.AutoField(primary_key = True)
    status = models.BooleanField('Status',default = True)
    creation_date = models.DateField('Creation Date',auto_now = False, auto_now_add = True)
    modification_date = models.DateField('Modification Date',auto_now = True, auto_now_add = False)
    elimination_date = models.DateField('Elimination Date',auto_now = True, auto_now_add = False)

    class Meta:
        abstract = True

class Category(ModelBase):
    name = models.CharField('Category Name', max_length = 100, unique = True)
    reference_image = models.ImageField('Reference Image',upload_to = 'categories')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Author(ModelBase):
    first_name = models.CharField('First Name',max_length = 100)
    last_name = models.CharField('Last Name',max_length = 120)
    email = models.EmailField('Email', max_length = 200)
    description = models.TextField('Description')
    reference_image = models.ImageField('Reference Image', null = True, blank = True,upload_to = 'authors/')
    web = models.URLField('Web', null = True, blank = True)
    facebook = models.URLField('Facebook', null = True, blank = True)
    twitter = models.URLField('Twitter', null = True, blank = True)
    instagram = models.URLField('Instagram', null = True, blank = True)
    linkedin = models.URLField('Linkedin', null = True, blank = True)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return '{0},{1}'.format(self.last_name,self.first_name)

class Post(models.Model):
    id = models.AutoField(primary_key = True)
    status = models.BooleanField('Status',default = True)
    creation_date = models.DateField('Creation Date',auto_now = False, auto_now_add = True)
    modification_date = models.DateField('Modification Date',auto_now = True, auto_now_add = False)
    elimination_date = models.DateField('Elimination Date',auto_now = True, auto_now_add = False)
    title = models.CharField('Post Title',max_length = 150, unique = True)
    slug = models.CharField('Slug', max_length = 150, unique = True)
    description = models.TextField('Description')
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    contents = RichTextField()
    reference_image = models.ImageField('Reference Image', upload_to = 'images/', max_length = 255)
    published = models.BooleanField('Published / Not Published',default = False)
    publication_date = models.DateField('Publication Date')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

class Web(ModelBase):
    about = models.TextField('About')
    phone = models.CharField('Phone', max_length = 20)
    email = models.EmailField('Email', max_length = 200)
    address = models.CharField('Address', max_length = 200)

    class Meta:
        verbose_name = 'Web'
        verbose_name_plural = 'Webs'

    def __str__(self):
        return self.about

class SocialMedia(ModelBase):
    facebook = models.URLField('Facebook')
    twitter = models.URLField('Twitter')
    instagram = models.URLField('Instagram')
    linkedin = models.URLField('Linkedin')

    class Meta:
        verbose_name = 'Social Media'
        verbose_name_plural = 'Social Media'

    def __str__(self):
        return self.facebook

class Contact(ModelBase):
    first_name = models.CharField('First Name', max_length = 100)
    last_name = models.CharField('Last Name', max_length = 150)
    email = models.EmailField('Email', max_length = 200)
    subject = models.CharField('Subject', max_length = 100)
    message = models.TextField('Message')

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.subject

class Subscriber(ModelBase):
    email = models.EmailField('Email', max_length = 200)

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'

    def __str__(self):
        return self.email

class Comment(models.Model):
    id = models.AutoField(primary_key = True)
    status = models.BooleanField('Status',default = True)
    creation_date = models.DateField('Creation Date',auto_now = False, auto_now_add = True)
    modification_date = models.DateField('Modification Date',auto_now = True, auto_now_add = False)
    elimination_date = models.DateField('Elimination Date',auto_now = True, auto_now_add = False)
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    email = models.EmailField('Email', max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField('Created Date',auto_now = False, auto_now_add = True)
    approved_comment = models.BooleanField(default=False)
    reference_image = models.ImageField('Reference Image', upload_to = 'images/', max_length = 255)


    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text