# Generated by Django 2.2.4 on 2019-08-24 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chair_mail', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submissionmessage',
            old_name='submissions_to',
            new_name='recipients',
        ),
        migrations.RenameField(
            model_name='usermessage',
            old_name='users_to',
            new_name='recipients',
        ),
    ]
