# Generated by Django 4.0.4 on 2022-05-07 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_rename_book_id_review_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='Book',
            new_name='book',
        ),
    ]
