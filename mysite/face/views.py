import random
import string

from django.http import Http404
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import EncryptionForm
from .forms import ShortenLinkForm, CommentForm
from .models import ShortenedLink, Comment, Resume, Headers, Encryption
from .utils import print_result


def index(request):
    resume_data = Resume.objects.first()
    headers_data = Headers.objects.first()
    return render(request, 'resume.html', {'resume_data': resume_data, 'headers_data': headers_data})


def contact(request):
    comments = Comment.objects.filter(approved=True)
    resume_data = Resume.objects.first()
    headers_data = Headers.objects.first()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CommentForm()

    return render(request, 'contact.html', {'form': form, 'comments': comments, 'resume_data': resume_data,
                                            'headers_data': headers_data})


def shorten_link(request):
    resume_data = Resume.objects.first()
    headers_data = Headers.objects.first()
    if request.method == 'POST':
        form = ShortenLinkForm(request.POST)
        if form.is_valid():
            original_link = form.cleaned_data['original_link']
            short_link = generate_short_link()
            ShortenedLink.objects.create(original_link=original_link, short_link=short_link)
            return render(request, 'shortened_link.html', {'short_link': short_link, 'resume_data': resume_data,
                                                           'headers_data': headers_data})
    else:
        form = ShortenLinkForm()
    return render(request, 'shorten_link.html', {'form': form, 'resume_data': resume_data,
                                                 'headers_data': headers_data})


def shorten(request):
    resume_data = Resume.objects.first()
    headers_data = Headers.objects.first()
    if request.method == 'POST':
        original_link = request.POST.get('original_link')
        if original_link:
            short_link = generate_short_link()
            ShortenedLink.objects.create(original_link=original_link, short_link=short_link)
            return render(request, 'shortened_link.html', {'short_link': short_link, 'resume_data': resume_data,
                                                           'headers_data': headers_data})
    return redirect('shorten_link')


def redirect_to_original(request, short_link):
    try:
        original_link = ShortenedLink.objects.get(short_link=short_link).original_link
        return redirect(original_link)
    except ShortenedLink.DoesNotExist:
        raise Http404("Shortened link does not exist")


def generate_short_link():
    characters = string.ascii_letters + string.digits
    while True:
        short_link = ''.join(random.choice(characters) for _ in range(6))
        if not ShortenedLink.objects.filter(short_link=short_link).exists():
            return short_link


def encryption(request):
    resume_data = Resume.objects.first()
    headers_data = Headers.objects.first()

    if request.method == 'POST':
        form = EncryptionForm(request.POST)
        if form.is_valid():
            key = form.cleaned_data['key']
            message = form.cleaned_data['text']
            action = request.POST.get('action')
            if action == 'encrypt':
                encrypted_text = print_result(key, message)
                encryption_entry = Encryption(key=key, text=message, ciphertext=encrypted_text)
                encryption_entry.save()
                return redirect('encrypted_text', encrypted_text=encrypted_text)
            elif action == 'decrypt':
                decrypt_text = Encryption.objects.filter(key=key, ciphertext=message).first()
                if decrypt_text:
                    return redirect('encrypted_text', encrypted_text=decrypt_text)
                else:
                    encrypted_text = print_result(key, message)
                    return redirect('encrypted_text', encrypted_text=encrypted_text)
    else:
        form = EncryptionForm()

    return render(request, 'encryption.html', {'form': form, 'resume_data': resume_data, 'headers_data': headers_data})


def encrypted_text_view(request, encrypted_text):
    resume_data = Resume.objects.first()
    headers_data = Headers.objects.first()
    return render(request, 'encrypted_text.html', {'encrypted_text': encrypted_text, 'resume_data': resume_data,
                                                   'headers_data': headers_data})
