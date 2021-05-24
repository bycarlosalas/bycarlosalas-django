from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category

class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author

class PostResource(resources.ModelResource):
    class Meta:
        model = Post

class ContactResource(resources.ModelResource):
    class Meta:
        model = Contact

class WebResource(resources.ModelResource):
    class Meta:
        model = Web

class SocialMediaResource(resources.ModelResource):
    class Meta:
        model = SocialMedia

class SubscriberResource(resources.ModelResource):
    class Meta:
        model = Subscriber

class CommentResource(resources.ModelResource):
    class Meta:
        model = Comment

class CategoryAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('name','status','creation_date')
    search_fields = ['name']
    resource_class = CategoryResource

class AuthorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('first_name','last_name','email','description','creation_date')
    search_fields = ['first_name','last_name','email']
    resource_class = AuthorResource

class PostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('title','published','author','description','status','publication_date')
    search_fields = ['title','author']
    resource_class = PostResource

class WebAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('about','email','address','phone','status','creation_date')
    search_fields = ['email']
    resource_class = WebResource


class SocialMediaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('facebook','twitter','instagram','status','creation_date')
    search_fields = ['facebook']
    resource_class = SocialMediaResource

class ContactAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('first_name','last_name','email','subject','message','status','creation_date')
    search_fields = ['email']
    resource_class = ContactResource

class SubscriberAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('email','status','creation_date')
    search_fields = ['email']
    resource_class = SubscriberResource

class CommentAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('post','author','text', 'created_date','creation_date')
    search_fields = ['email']
    resource_class = CommentResource

admin.site.register(Category,CategoryAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Web,WebAdmin)
admin.site.register(SocialMedia,SocialMediaAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Subscriber,SubscriberAdmin)
admin.site.register(Comment,CommentAdmin)