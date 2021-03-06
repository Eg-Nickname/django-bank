# Generated by Django 4.0 on 2022-01-18 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0002_remove_exchangelisting_ratio_exchangelisting_rati_to_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exchangelisting',
            old_name='rati_to',
            new_name='ratio_to',
        ),
        migrations.RemoveField(
            model_name='exchangelisting',
            name='amount',
        ),
        migrations.AddField(
            model_name='exchangelisting',
            name='amount_owned',
            field=models.PositiveIntegerField(default=0, verbose_name='Kwota1'),
        ),
        migrations.AddField(
            model_name='exchangelisting',
            name='amount_wanted',
            field=models.PositiveIntegerField(default=0, verbose_name='Kwota2'),
        ),
        migrations.AddField(
            model_name='exchangelisting',
            name='is_fixed',
            field=models.BooleanField(default=False),
        ),
    ]
