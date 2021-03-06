# Generated by Django 3.1 on 2020-09-29 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('date', models.DateField()),
                ('topics', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=400)),
                ('articleType', models.CharField(max_length=50)),
                ('authors', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
    ]
