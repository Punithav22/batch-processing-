# Generated by Django 5.1.4 on 2025-02-24 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batch1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailedData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=255)),
                ('field2', models.CharField(max_length=255)),
                ('field3', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255, verbose_name='Full Name')),
                ('description', models.TextField(verbose_name='Description')),
            ],
        ),
        migrations.AlterField(
            model_name='csvdata',
            name='field1',
            field=models.CharField(max_length=255, verbose_name='Field One'),
        ),
        migrations.AlterField(
            model_name='csvdata',
            name='field2',
            field=models.CharField(max_length=255, verbose_name='Field Two'),
        ),
        migrations.AlterField(
            model_name='csvdata',
            name='field3',
            field=models.CharField(max_length=255, verbose_name='Field Three'),
        ),
    ]
