# Generated by Django 2.2.6 on 2019-11-11 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_auto_20191110_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='cnpj',
            field=models.CharField(default=1, max_length=14),
            preserve_default=False,
        ),
    ]
