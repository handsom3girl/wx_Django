# Generated by Django 2.0 on 2020-04-28 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0007_doubantask_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='doubansubject',
            name='peoplenum',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='doubansubject',
            name='score',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='doubansubject',
            name='star_five',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='doubansubject',
            name='star_four',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='doubansubject',
            name='star_one',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='doubansubject',
            name='star_three',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='doubansubject',
            name='star_two',
            field=models.CharField(default='', max_length=10),
        ),
    ]
