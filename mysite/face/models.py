from django.db import models


class ShortenedLink(models.Model):
    original_link = models.URLField()
    short_link = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.short_link


class Comment(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255, default="Anonymous")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.name


class Resume(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    date_of_birth = models.DateField()

    education = models.TextField()
    work_experience = models.TextField()
    skills = models.TextField()
    about_me = models.TextField()
    description = models.TextField()
    technologies = models.TextField()

    def __str__(self):
        return "Resume"


class Headers(models.Model):
    resume = models.CharField(max_length=20)

    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    date_of_birth = models.CharField(max_length=20)

    education = models.CharField(max_length=20)
    experience = models.CharField(max_length=20)
    skills = models.CharField(max_length=20)
    about_me = models.CharField(max_length=20)

    projects = models.CharField(max_length=20)

    site_code_in_github = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    features = models.CharField(max_length=20)
    technologies = models.CharField(max_length=20)
    goal = models.CharField(max_length=20)
    project_link = models.CharField(max_length=20)
    enter_link_to_shorten = models.CharField(max_length=30)

    leave_feedback = models.CharField(max_length=20)
    change_language = models.CharField(max_length=20)

    footer = models.TextField()

    reduce = models.CharField(max_length=20)
    submit_comment = models.CharField(max_length=20)

    def __str__(self):
        return "Header"
