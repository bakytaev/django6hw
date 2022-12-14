# Generated by Django 3.2 on 2022-08-27 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('mentor_name', models.CharField(max_length=128)),
                ('language', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('laptop', models.CharField(max_length=128)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codify.course')),
            ],
        ),
    ]
