# Generated by Django 5.0a1 on 2023-09-22 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonAPI', '0004_remove_order_user_alter_order_delivery_crew'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='orderitem',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
    ]
