# Generated by Django 4.2 on 2023-04-06 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0004_tg_employee_tg_employee_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tg_employee',
            name='tg_employee_gender',
            field=models.TextField(default='O', help_text='genero del empleado', max_length=1),
        ),
    ]
