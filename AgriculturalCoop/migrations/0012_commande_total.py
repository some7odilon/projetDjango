# Generated by Django 5.1.1 on 2024-10-05 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgriculturalCoop', '0011_remove_commande_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='total',
            field=models.CharField(default='500', max_length=500),
            preserve_default=False,
        ),
    ]
