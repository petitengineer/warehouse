# Generated by Django 4.0.4 on 2022-05-24 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0006_delete_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='collection',
        ),
        migrations.DeleteModel(
            name='Collection',
        ),
    ]
