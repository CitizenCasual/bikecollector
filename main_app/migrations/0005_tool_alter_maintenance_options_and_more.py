# Generated by Django 4.0.3 on 2022-04-11 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_maintenance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('use', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='maintenance',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='date',
            field=models.DateField(verbose_name='Maintenance date'),
        ),
    ]
