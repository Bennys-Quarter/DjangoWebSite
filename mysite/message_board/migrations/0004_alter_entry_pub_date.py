# Generated by Django 4.1.5 on 2023-01-07 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_board', '0003_alter_entry_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='pub_date',
            field=models.DateField(),
        ),
    ]
