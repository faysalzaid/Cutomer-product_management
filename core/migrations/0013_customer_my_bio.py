# Generated by Django 3.1.7 on 2021-04-08 16:32

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20210407_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='my_bio',
            field=django_quill.fields.QuillField(blank=True, null=True),
        ),
    ]
