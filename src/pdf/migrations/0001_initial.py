# Generated by Django 3.2.12 on 2022-02-17 11:15

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import fernet_fields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GenericConfig',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('data', fernet_fields.fields.EncryptedTextField()),
                ('uploader_ref', models.CharField(blank=True, choices=[('minio', 'Minio')], max_length=20, null=True)),
                ('shotener_ref', models.CharField(blank=True, choices=[('yaus', 'YAUS')], max_length=20, null=True)),
                ('retries', models.IntegerField(default=0)),
                ('max_concurrency', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Generic Config',
                'verbose_name_plural': 'Generic Configs',
                'db_table': 'GenericConfig',
            },
        ),
        migrations.CreateModel(
            name='Pdf',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.UUIDField(primary_key=True, serialize=False, unique=True)),
                ('meta', models.JSONField(blank=True, null=True)),
                ('data', models.JSONField(blank=True, null=True)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20), null=True, size=None)),
                ('url', models.CharField(blank=True, max_length=200)),
                ('url_meta', models.JSONField()),
                ('url_expiry', models.DateTimeField(null=True)),
                ('short_url', models.CharField(blank=True, max_length=50)),
                ('status', models.CharField(choices=[('Queued', 'Queued'), ('Processing', 'Processing'), ('Failed', 'Failed'), ('Complete', 'Complete'), ('Error', 'Error')], default='Queued', max_length=20)),
                ('step', models.CharField(choices=[('Not Started', 'Not Started'), ('Data Fetching', 'Data Fetching'), ('Mapping Fetching', 'Mapping Fetching'), ('Template Processing', 'Template Processing'), ('PDF Building', 'PDF Building'), ('Uploading', 'Uploading'), ('URL Shortening', 'URL Shortening'), ('Deleted From Drive', 'Deleted From Drive')], default='Not Started', max_length=30)),
                ('tries', models.IntegerField(default=0)),
                ('version', models.CharField(max_length=5)),
                ('config', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='pdf.genericconfig')),
            ],
            options={
                'verbose_name': 'PDF',
                'verbose_name_plural': 'PDFs',
                'db_table': 'Pdf',
            },
        ),
        migrations.CreateModel(
            name='Audit',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('status', models.CharField(choices=[('Queued', 'Queued'), ('Processing', 'Processing'), ('Failed', 'Failed'), ('Complete', 'Complete'), ('Error', 'Error'), ('None', 'None')], default='None', max_length=20)),
                ('stacktrace', models.JSONField(null=True)),
                ('pdf', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='pdf.pdf')),
            ],
            options={
                'verbose_name': 'Audit',
                'verbose_name_plural': 'Audits',
                'db_table': 'Audit',
            },
        ),
    ]
