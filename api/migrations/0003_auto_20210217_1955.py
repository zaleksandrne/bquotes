# Generated by Django 3.0.5 on 2021-02-17 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_quote_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='api/media/', verbose_name='Изображение публикации'),
        ),
    ]