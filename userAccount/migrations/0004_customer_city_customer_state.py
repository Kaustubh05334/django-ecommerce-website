# Generated by Django 4.2.3 on 2023-07-14 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAccount', '0003_alter_customer_cart_items_alter_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(default='jaipur', max_length=20),
        ),
        migrations.AddField(
            model_name='customer',
            name='state',
            field=models.CharField(default='rajasthan', max_length=20),
        ),
    ]