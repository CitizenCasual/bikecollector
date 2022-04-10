# Generated by Django 4.0.3 on 2022-04-10 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='type',
            field=models.CharField(choices=[('Mountain', 'M'), ('Road', 'R'), ('Gravel', 'G')], default='Mountain', max_length=8),
        ),
    ]