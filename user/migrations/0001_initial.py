# Generated by Django 4.1.2 on 2022-11-16 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Iletisim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=100)),
                ('soyad', models.CharField(max_length=100)),
                ('eposta', models.EmailField(max_length=100)),
                ('telefon', models.CharField(max_length=11)),
                ('mesaj', models.TextField(max_length=500)),
            ],
        ),
    ]
