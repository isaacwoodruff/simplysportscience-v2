# Generated by Django 2.2.7 on 2019-11-25 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20191118_1618'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['-created_date']},
        ),
    ]
