# Generated by Django 2.2.6 on 2019-11-24 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0003_store_cnpj'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Retail',
            new_name='Retailer',
        ),
    ]