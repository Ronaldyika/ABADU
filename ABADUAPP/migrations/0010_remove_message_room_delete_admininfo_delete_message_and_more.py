# Generated by Django 4.2.4 on 2023-09-02 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ABADUAPP', '0009_room_rename_content_message_message_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='room',
        ),
        migrations.DeleteModel(
            name='Admininfo',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]
