from modeltranslation.translator import register, TranslationOptions
from .models import Resume, Headers


@register(Resume)
class ResumeTranslationOptions(TranslationOptions):
    fields = ('name', 'phone', 'email', 'date_of_birth', 'education', 'work_experience', 'skills', 'about_me',
              'description', 'technologies', 'encrypt_text')


@register(Headers)
class HeadersTranslationOptions(TranslationOptions):
    fields = ('resume', 'name', 'phone', 'email', 'date_of_birth', 'education', 'experience', 'skills', 'about_me',
              'projects', 'site_code_in_github', 'description', 'features', 'technologies', 'goal', 'project_link',
              'enter_link_to_shorten', 'leave_feedback', 'change_language', 'footer', 'reduce', 'submit_comment',
              'text_encryption', 'key', 'message', 'encrypt', 'actions', 'company', 'shortened_link')
