from django import forms
from django.core.exceptions import ValidationError

from .models import Comment, Encryption


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


class EncryptionForm(forms.ModelForm):
    class Meta:
        model = Encryption
        fields = ['key', 'text']
        widgets = {
            'key': forms.TextInput(attrs={'class': 'key-input'}),
            'text': forms.Textarea(attrs={'class': 'text-input', 'cols': 60, 'rows': 10})
        }

    def clean_key(self):
        key = self.cleaned_data['key']
        if type(key) != int:
            raise ValidationError('Key should be integer')
        return key
