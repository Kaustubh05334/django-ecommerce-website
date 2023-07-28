# Generated by Django 4.2.3 on 2023-07-15 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_qty'),
        ('userAccount', '0004_customer_city_customer_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField()),
                ('mode_of_payment', models.CharField(choices=[('cash_on_delivery', 'Cash on Delivery'), ('debit_card', 'Debit Card'), ('credit_card', 'Credit Card'), ('upi', 'UPI')], max_length=20)),
                ('order_status', models.CharField(choices=[('processing', 'Processing'), ('shipped', 'Shipped'), ('out_for_delivery', 'Out for Delivery'), ('delivered', 'Delivered')], max_length=20)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='userAccount.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.product')),
            ],
        ),
    ]
