# Generated by Django 4.1.3 on 2022-12-06 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_bed_name_alter_bed_memo'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='archive',
            field=models.BooleanField(default=False),
        ),
    ]
