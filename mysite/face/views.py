import random
import string

from django.http import Http404
from django.shortcuts import render, redirect

from .forms import ShortenLinkForm, CommentForm
from .models import ShortenedLink, Comment


def index(request):
    return render(request, "resume.html")


def contact(request):
    comments = Comment.objects.filter(approved=True)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CommentForm()

    return render(request, 'contact.html', {'form': form, 'comments': comments})


def shorten_link(request):
    if request.method == 'POST':
        form = ShortenLinkForm(request.POST)
        if form.is_valid():
            original_link = form.cleaned_data['original_link']
            short_link = generate_short_link()
            ShortenedLink.objects.create(original_link=original_link, short_link=short_link)
            return render(request, 'shortened_link.html', {'short_link': short_link})
    else:
        form = ShortenLinkForm()
    return render(request, 'shorten_link.html', {'form': form})


def shorten(request):
    if request.method == 'POST':
        original_link = request.POST.get('original_link')
        if original_link:
            short_link = generate_short_link()
            ShortenedLink.objects.create(original_link=original_link, short_link=short_link)
            return render(request, 'shortened_link.html', {'short_link': short_link})
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
