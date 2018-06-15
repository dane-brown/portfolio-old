# Generated by Django 2.0.6 on 2018-06-14 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('image', models.FileField(default='', upload_to='')),
                ('category', models.CharField(default='', max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]