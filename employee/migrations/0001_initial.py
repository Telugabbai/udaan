# Generated by Django 2.2 on 2020-02-16 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=15)),
                ('salary', models.IntegerField()),
                ('city', models.CharField(max_length=20)),
                ('dept', models.CharField(max_length=20)),
            ],
        ),
    ]
