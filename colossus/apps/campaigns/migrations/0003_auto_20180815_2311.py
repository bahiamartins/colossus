# Generated by Django 2.1 on 2018-08-15 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0002_auto_20180812_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='email',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='links', to='campaigns.Email', verbose_name='email'),
        ),
    ]
