# Generated by Django 4.2.3 on 2024-01-04 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0023_headers_encrypt_en_headers_encrypt_uk_headers_key_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='headers',
            name='actions',
            field=models.CharField(default=0, max_length=35),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='headers',
            name='actions_en',
            field=models.CharField(max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='headers',
            name='actions_uk',
            field=models.CharField(max_length=35, null=True),
        ),
    ]
