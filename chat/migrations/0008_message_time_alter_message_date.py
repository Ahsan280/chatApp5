# Generated by Django 5.0.1 on 2024-04-09 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_remove_message_time_alter_message_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
