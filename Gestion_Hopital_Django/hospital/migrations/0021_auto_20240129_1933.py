# Generated by Django 3.0.5 on 2024-01-29 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0020_auto_20240129_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symptomes',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
