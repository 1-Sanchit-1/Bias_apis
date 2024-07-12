# Generated by Django 5.0.6 on 2024-07-12 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFormSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=15)),
                ('select_time', models.CharField(max_length=10)),
                ('selected_day', models.DateField()),
            ],
        ),
    ]
