# Generated by Django 5.0.2 on 2024-02-15 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
