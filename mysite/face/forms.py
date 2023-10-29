from django import forms
from .models import Comment


class ShortenLinkForm(forms.Form):
    original_link = forms.URLField(label="Original link")


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
