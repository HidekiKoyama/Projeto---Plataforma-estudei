# Generated by Django 4.2.2 on 2023-07-06 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0019_alter_courses_delete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorie_curses',
            old_name='active',
            new_name='delete',
        ),
    ]
