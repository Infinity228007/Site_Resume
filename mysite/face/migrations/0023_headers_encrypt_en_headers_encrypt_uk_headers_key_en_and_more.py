# Generated by Django 4.2.3 on 2024-01-04 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0022_headers_encrypt_headers_key_headers_message_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='headers',
            name='encrypt_en',
            field=models.CharField(max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='headers',
            name='encrypt_uk',
            field=models.CharField(max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='headers',
            name='key_en',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='headers',
            name='key_uk',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='headers',
            name='message_en',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='headers',
            name='message_uk',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='headers',
            name='text_encryption_en',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='headers',
            name='text_encryption_uk',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='encrypt_text_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='encrypt_text_uk',
            field=models.TextField(null=True),
        ),
    ]
