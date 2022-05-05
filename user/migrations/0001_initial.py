# Generated by Django 4.0.4 on 2022-04-30 11:11

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('price', models.TextField(max_length=10)),
                ('description', models.TextField(max_length=250, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=user.models.filepath)),
            ],
        ),
    ]