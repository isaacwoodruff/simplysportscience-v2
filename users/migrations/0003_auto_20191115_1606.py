# Generated by Django 2.2.7 on 2019-11-15 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191115_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateprofile',
            name='is_candidate',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='employerprofile',
            name='is_employer',
            field=models.BooleanField(default=True),
        ),
    ]