# Generated by Django 3.1.4 on 2021-01-28 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webserver', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
            ],
        ),
    ]