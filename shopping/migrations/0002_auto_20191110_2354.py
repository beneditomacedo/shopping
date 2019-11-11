# Generated by Django 2.2.6 on 2019-11-10 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Retail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='store',
            name='retail',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shopping.Retail'),
            preserve_default=False,
        ),
    ]