# Generated by Django 4.0.2 on 2022-02-24 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Directory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
                ('Number', models.TextField()),
                ('Email', models.EmailField(max_length=254)),
                ('Position', models.TextField()),
            ],
        ),
    ]