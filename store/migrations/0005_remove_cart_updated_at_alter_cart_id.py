# Generated by Django 5.1.2 on 2024-11-07 23:36

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
