# Generated by Django 5.1.1 on 2024-10-04 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgriculturalCoop', '0008_alter_commande_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='commande',
            name='code_postal',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='commande',
            name='items',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='commande',
            name='nom',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='commande',
            name='pays',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='commande',
            name='ville',
            field=models.CharField(max_length=200),
        ),
    ]
