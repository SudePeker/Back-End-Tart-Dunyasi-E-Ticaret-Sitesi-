# Generated by Django 4.1.2 on 2022-11-15 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0005_alter_urun_sub_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urun',
            name='sub_category',
            field=models.ManyToManyField(blank=True, to='urunler.altkategori'),
        ),
    ]