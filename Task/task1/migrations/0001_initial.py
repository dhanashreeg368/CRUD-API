# Generated by Django 4.0.4 on 2022-05-24 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='task1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('age', models.IntegerField(max_length=3)),
                ('dob', models.DateField(max_length=8)),
            ],
        ),
    ]
