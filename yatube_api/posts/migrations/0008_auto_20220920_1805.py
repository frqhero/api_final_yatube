# Generated by Django 2.2.16 on 2022-09-20 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20220920_1729'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique follow',
        ),
    ]
