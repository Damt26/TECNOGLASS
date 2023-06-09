# Generated by Django 4.2 on 2023-04-06 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0003_alter_tg_employee_tg_employee_update_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tg_employee',
            name='tg_employee_email',
            field=models.TextField(help_text='correo del empleado', null=True),
        ),
        migrations.AddField(
            model_name='tg_employee',
            name='tg_employee_gender',
            field=models.TextField(default='O', help_text='genero del empleado', max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='tg_employee',
            name='tg_employee_id',
            field=models.TextField(default='999999999999', help_text='identificacion del empleado', max_length=12),
        ),
    ]
