# Generated by Django 4.2 on 2023-04-05 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tg_social_security',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_social_security_name', models.TextField(help_text='Nombre de la EPS', max_length=15)),
                ('tg_social_security_nit', models.TextField(help_text='NIT de la empresa', max_length=9)),
                ('tg_social_security_contact', models.TextField(help_text='Telefono de la empresa', max_length=10)),
                ('tg_social_security_city', models.TextField(help_text='Ciudad de la empresa', max_length=20)),
                ('tg_social_security_active', models.BooleanField(default=True, help_text='Activo en sistema?')),
                ('tg_social_security_create', models.DateTimeField(help_text='Fecha de ingreso de la empresa')),
                ('tg_social_security_update', models.DateTimeField(help_text='Fecha de actualización de la empresa')),
                ('tg_social_security_delete', models.DateTimeField(help_text='Fecha de retiro de la empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Tg_employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_employee_name', models.TextField(help_text='Nombre del empleado', max_length=20)),
                ('tg_employee_lastname', models.TextField(help_text='Primer apellido del empleado', max_length=20)),
                ('tg_employee_surname', models.TextField(help_text='Segundo apellido del empleado', max_length=20)),
                ('tg_employee_work_area', models.TextField(help_text='Segundo apellido del empleado', max_length=20)),
                ('tg_employee_birthday', models.DateTimeField(help_text='Fecha de nacimiento del empleado')),
                ('tg_employee_birthplace', models.TextField(help_text='Lugar de nacimiento del empleado', max_length=15)),
                ('tg_employee_phone', models.TextField(help_text='Telefono del empleado', max_length=10)),
                ('tg_employee_address', models.TextField(help_text='Direccion del empleado', max_length=40)),
                ('tg_employee_city', models.TextField(help_text='Ciudad del empleado', max_length=15)),
                ('tg_employee_distric', models.TextField(help_text='Barrio del empleado', max_length=20)),
                ('tg_employee_active', models.BooleanField(default=True, help_text='Activo en sistema?')),
                ('tg_employee_create', models.DateTimeField(help_text='Fecha de ingreso del empleado')),
                ('tg_employee_update', models.DateTimeField(help_text='Fecha de actualización del empleado')),
                ('tg_employee_delete', models.DateTimeField(help_text='Fecha de retiro del empleado')),
                ('tg_social_security', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.tg_social_security')),
            ],
        ),
    ]
