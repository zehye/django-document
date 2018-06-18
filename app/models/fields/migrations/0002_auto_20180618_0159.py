# Generated by Django 2.0.6 on 2018-06-18 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='shirt_size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], help_text='S는 작음', max_length=1, verbose_name='셔츠 사이즈'),
        ),
    ]
