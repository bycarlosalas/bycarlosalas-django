from django import forms
from .models import Post,Contact,Comment

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ('status',)

        widgets = {
            'first-name':forms.TextInput(
                attrs = {
                }
            ),
            'last-name':forms.TextInput(
                attrs = {
                }
            ),
            'email':forms.EmailInput(
                attrs = {
                }
            ),
            'subject':forms.TextInput(
                attrs = {
                }
            ),
            'message':forms.Textarea(
                attrs = {
                }
            ),
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'