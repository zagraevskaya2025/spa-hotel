# Generated by Django 3.2 on 2025-04-07 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='description',
            field=models.TextField(default='Без описания', verbose_name='Описание'),
            preserve_default=False,
        ),
    ]
