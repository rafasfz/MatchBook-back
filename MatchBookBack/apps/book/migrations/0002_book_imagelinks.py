# Generated by Django 4.1.3 on 2022-12-04 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='imageLinks',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
