from django import forms
from .models import Comment


class ShortenLinkForm(forms.Form):
    original_link = forms.URLField(label='original_link')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'company', 'text']
        error_messages = {
            'name': {
                'required': 'Please enter your name.'
            },
            'company': {
                'required': 'Please enter your company name.'
            },
            'text': {
                'required': 'Please enter comment text.'
            }
        }


class EncryptionForm(forms.Form):
    key = forms.CharField(label='Key', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)
