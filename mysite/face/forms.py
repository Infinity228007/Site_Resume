from django import forms
from .models import Comment


class ShortenLinkForm(forms.Form):
    original_link = forms.URLField(label="Оригинальная ссылка")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'company', 'text']
        labels = {
            'name': 'Имя',
            'company': 'Компания',
            'text': 'Текст',
        }
        error_messages = {
            'name': {
                'required': 'Пожалуйста, введите ваше имя.'
            },
            'company': {
                'required': 'Пожалуйста, введите название компании.'
            },
            'text': {
                'required': 'Пожалуйста, введите текст комментария.'
            }
        }
