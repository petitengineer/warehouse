# Generated by Django 4.0.4 on 2022-05-22 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0003_add_slug_to_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip_code',
            field=models.TextField(default='ERROR', max_length=10),
        ),
        migrations.AddField(
            model_name='product',
            name='warehouse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='warehouse.warehouse'),
        ),
    ]
