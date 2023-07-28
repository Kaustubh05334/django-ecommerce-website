# Generated by Django 4.2.3 on 2023-07-13 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_product_seller'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_or_company_name', models.CharField(max_length=50)),
                ('GST_number', models.CharField(max_length=20)),
                ('shop_address', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]