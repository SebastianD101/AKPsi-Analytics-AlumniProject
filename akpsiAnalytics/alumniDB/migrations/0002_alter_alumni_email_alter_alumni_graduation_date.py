# Generated by Django 4.1.6 on 2023-02-27 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumniDB', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumni',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='graduation_date',
            field=models.IntegerField(),
        ),
    ]
