# Generated by Django 5.0.7 on 2024-08-10 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='schedule',
            field=models.CharField(max_length=255),
        ),
    ]
