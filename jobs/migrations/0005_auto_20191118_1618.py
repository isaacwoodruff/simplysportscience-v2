# Generated by Django 2.2.7 on 2019-11-18 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20191116_1600'),
        ('jobs', '0004_auto_20191118_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='user_fk',
        ),
        migrations.AddField(
            model_name='job',
            name='employer_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.EmployerProfile'),
        ),
    ]
