# Generated by Django 2.0.2 on 2019-04-16 18:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produkty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(max_length=250)),
                ('data', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('treść', models.TextField()),
                ('obrazek', models.ImageField(upload_to='images/')),
            ],
        ),
    ]