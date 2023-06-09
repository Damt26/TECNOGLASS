# Generated by Django 4.2 on 2023-04-09 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0010_alter_tg_social_security_tg_social_security_update'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tg_city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_city_name', models.TextField(help_text='Nombre de la ciudad', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tg_gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_gender_name', models.TextField(help_text='Nombre de la ciudad', max_length=1)),
            ],
        ),
    ]
