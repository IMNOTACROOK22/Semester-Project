# Generated by Django 4.1.1 on 2022-11-22 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_coupon_percentdiscount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Coupon',
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
