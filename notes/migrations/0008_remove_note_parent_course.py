# Generated by Django 4.0.4 on 2022-05-05 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_course_alter_comment_created_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='parent_course',
        ),
    ]
