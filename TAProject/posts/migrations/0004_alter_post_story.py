# Generated by Django 4.0.6 on 2022-08-01 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_photo_alter_post_user_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='story',
            field=models.TextField(max_length=400, null=True),
        ),
    ]
