# Generated by Django 5.0.2 on 2024-12-05 21:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_wishlist'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=150)),
                ('lname', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=150)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=150)),
                ('pincode', models.CharField(max_length=150)),
                ('total_price', models.FloatField()),
                ('payment_mode', models.CharField(max_length=150)),
                ('payment_id', models.CharField(max_length=150, null=True)),
                ('status', models.TextField(choices=[('Pending', 'Pending'), ('Out For Shipping', 'Out For Shipping'), ('Completed', 'Completed')], default='Pending', max_length=150)),
                ('message', models.TextField(null=True)),
                ('tracking_no', models.CharField(max_length=150, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]
