# Generated by Django 4.2.3 on 2023-10-17 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0007_remove_comment_author_comment_company_comment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
