# Generated by Django 5.1.3 on 2024-12-19 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiClass', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, null=True)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
