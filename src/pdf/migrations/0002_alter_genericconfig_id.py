# Generated by Django 3.2.12 on 2022-02-17 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericconfig',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
