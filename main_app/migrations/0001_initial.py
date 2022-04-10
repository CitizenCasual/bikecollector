# Generated by Django 4.0.3 on 2022-04-10 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('M', 'Mountain'), ('R', 'Road'), ('G', 'Gravel')], default='M', max_length=1)),
                ('make', models.CharField(max_length=25)),
                ('model', models.CharField(max_length=25)),
                ('description', models.TextField(max_length=100)),
                ('year', models.IntegerField()),
            ],
        ),
    ]