# Generated by Django 4.2.1 on 2023-07-02 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0016_alter_courses_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]