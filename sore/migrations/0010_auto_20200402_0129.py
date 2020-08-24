# Generated by Django 3.0.4 on 2020-04-02 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sore', '0009_question_two_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='question',
            name='two_more',
            field=models.BooleanField(default=0, verbose_name='Имеет два и более ответов'),
        ),
    ]