# Generated by Django 2.2.2 on 2019-06-18 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20190618_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='password',
            field=models.CharField(default='fffff', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='details',
            name='username',
            field=models.CharField(default='aaaaaa', max_length=100),
            preserve_default=False,
        ),
    ]
