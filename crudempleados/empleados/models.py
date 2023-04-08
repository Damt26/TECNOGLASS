from django.db import models
from django.utils import timezone
# Create your models here.


class Tg_social_security(models.Model):
    tg_social_security_name = models.TextField(
        max_length=15, help_text='Nombre de la EPS', null=False)
    tg_social_security_nit = models.TextField(
        max_length=9, help_text='NIT de la empresa', null=False)
    tg_social_security_contact = models.TextField(
        max_length=10, help_text='Telefono de la empresa', null=False)
    tg_social_security_city = models.TextField(
        max_length=20, help_text='Ciudad de la empresa', null=False)
    tg_social_security_email = models.EmailField(
        default='test@gmail.com', help_text='Correo de la empresa', null=False)
    tg_social_security_active = models.BooleanField(
        default=True, help_text='Activo en sistema?')
    tg_social_security_create = models.DateTimeField(
        help_text='Fecha de ingreso de la empresa', null=True)
    tg_social_security_update = models.DateTimeField(
        help_text='Fecha de actualización de la empresa', null=True)
    tg_social_security_delete = models.DateTimeField(
        help_text='Fecha de retiro de la empresa', null=True)

    def __str__(self):
        return self.tg_social_security_name + self.tg_social_security_contact


class Tg_employee(models.Model):
    tg_employee_name = models.TextField(
        max_length=20, help_text='Nombre del empleado', null=False)
    tg_employee_lastname = models.TextField(
        max_length=20, help_text='Primer apellido del empleado', null=False)
    tg_employee_surname = models.TextField(
        max_length=20, help_text='Segundo apellido del empleado', null=True)
    tg_employee_work_area = models.TextField(
        max_length=20, help_text='Area de trabajo del empleado', null=True)
    tg_employee_id_type = models.TextField(
        max_length=2, default='cc', help_text='tipo de identificacion del empleado', null=False)
    tg_employee_id = models.TextField(
        max_length=12, default='999999999999', help_text='identificacion del empleado', null=False)
    tg_employee_email = models.TextField(
        help_text='correo del empleado', null=True)
    tg_employee_gender = models.TextField(
        max_length=1, default='O', help_text='genero del empleado', null=False)
    tg_employee_birthday = models.DateTimeField(
        help_text='Fecha de nacimiento del empleado', null=False)
    tg_employee_birthplace = models.TextField(
        max_length=15, help_text='Lugar de nacimiento del empleado', null=False)
    tg_social_security = models.ForeignKey(
        Tg_social_security, on_delete=models.CASCADE)
    tg_employee_phone = models.TextField(
        max_length=10, help_text='Telefono del empleado', null=False)
    tg_employee_address = models.TextField(
        max_length=40, help_text='Direccion del empleado', null=False)
    tg_employee_city = models.TextField(
        max_length=15, help_text='Ciudad del empleado', null=False)
    tg_employee_distric = models.TextField(
        max_length=20, help_text='Barrio del empleado', null=True)
    tg_employee_active = models.BooleanField(
        default=True, help_text='Activo en sistema?')
    tg_employee_create = models.DateTimeField(
        help_text='Fecha de ingreso del empleado', null=True)
    tg_employee_update = models.DateTimeField(
        help_text='Fecha de actualización del empleado', default=timezone.now)
    tg_employee_delete = models.DateTimeField(
        help_text='Fecha de retiro del empleado', null=True)

    def __str__(self):
        return self.tg_employee_name + self.tg_employee_lastname + self.tg_employee_surname
