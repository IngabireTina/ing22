# Generated by Django 3.0.8 on 2020-08-03 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200803_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, default='tina.jpg', null=True, upload_to=''),
        ),
    ]
