from datetime import tzinfo
from django.shortcuts import get_object_or_404, redirect, render
from empleados.models import Tg_employee, Tg_social_security
from django.utils.datetime_safe import datetime
# Create your views here.

from django.utils import timezone


def home(request):
    employee = Tg_employee.objects.all()
    context = {
        "employees": employee
    }
    return render(request, "employees.html", context)


def social_security(request):
    ss = Tg_social_security.objects.all()
    context = {
        "soc_sec": ss
    }
    return render(request, "socsec.html", context)


def social_security_detail(request, ss_pk):
    ss = Tg_social_security.objects.get(pk=ss_pk)
    context = {
        "soc_sec": ss
    }
    return render(request, "ss_detail.html", context)


def employee_detail(request, employee_pk):
    employee = Tg_employee.objects.get(pk=employee_pk)
    context = {
        "employee": employee
    }

    return render(request, "employee_detail.html", context)


def employee_delete(request, employee_pk):
    employee = Tg_employee.objects.get(pk=employee_pk)
    employee.tg_employee_active = False
    employee.tg_employee_update = timezone.now()
    employee.tg_employee_delete = timezone.now()
    employee.save()
    return redirect('/')


def social_security_delete(request, ss_pk):
    ss = Tg_social_security.objects.get(pk=ss_pk)
    ss.tg_social_security_active = False
    ss.tg_social_security_update = timezone.now()
    ss.tg_social_security_delete = timezone.now()

    ss.save()

    return redirect('/social_security')


def employee_creation(request):
    context = {
        "ss": Tg_social_security.objects.all()
    }
    try:
        if request.method == "POST":
            em = Tg_employee()
            em.tg_employee_name = request.POST.get('tg_employee_name')
            em.tg_employee_lastname = request.POST.get('tg_employee_lastname')
            em.tg_employee_surname = request.POST.get('tg_employee_surname')
            em.tg_employee_work_area = request.POST.get(
                'tg_employee_work_area')
            em.tg_employee_birthday = request.POST.get('tg_employee_birthday')
            em.tg_employee_birthplace = request.POST.get(
                'tg_employee_birthplace')
            em.tg_employee_phone = request.POST.get('tg_employee_phone')
            em.tg_employee_city = request.POST.get('tg_employee_city')
            em.tg_employee_distric = request.POST.get('tg_employee_distric')
            em.tg_employee_create = timezone.now()
            em.tg_employee_update = timezone.now()
            em.tg_social_security = Tg_social_security.objects.get(
                pk=request.POST.get('tg_social_security'))
            em.tg_employee_id_type = request.POST.get('tg_employee_id_type')
            em.tg_employee_id = request.POST.get('tg_employee_id')
            em.tg_employee_email = request.POST.get('tg_employee_email')
            em.tg_employee_gender = request.POST.get('tg_employee_gender')
            em.save()
            return redirect('/')

    except Exception as e:
        return e
    return render(request, "employees_create.html", context)


def social_security_creation(request):
    if request.method == "POST":
        try:
            ss = Tg_social_security()
            ss.tg_social_security_name = request.POST.get(
                'tg_social_security_name')
            ss.tg_social_security_nit = request.POST.get(
                'tg_social_security_nit')
            ss.tg_social_security_contact = request.POST.get(
                'tg_social_security_contact')
            ss.tg_social_security_city = request.POST.get(
                'tg_social_security_city')
            ss.tg_social_security_create = timezone.now()
            ss.tg_social_security_update = timezone.now()
            ss.save()
            return redirect('/')

        except Exception as e:
            return (e)

    return render(request, 'ss_create.html')


def social_security_update(request, ss_pk):
    ss = Tg_social_security.objects.get(pk=ss_pk)
    context = {
        "soc_sec": ss
    }
    if request.method == "POST":
        try:
            ss.tg_social_security_name = request.POST.get(
                'tg_social_security_name')
            ss.tg_social_security_nit = request.POST.get(
                'tg_social_security_nit')
            ss.tg_social_security_contact = request.POST.get(
                'tg_social_security_contact')
            ss.tg_social_security_city = request.POST.get(
                'tg_social_security_city')
            ss.tg_social_security_update = timezone.now()
            ss.save(force_update=True)

            return redirect('/')
        except Exception as e:
            return (e)

    return render(request, 'ss_update.html', context)


def employee_update(request, employee_pk):
    employee = Tg_employee.objects.get(pk=employee_pk)
    ss = Tg_social_security.objects.all()
    context = {
        "employee": employee,
        "ss": ss
    }
    try:
        if request.method == "POST":
            employee.tg_employee_name = employee.tg_employee_name
            employee.tg_employee_lastname = employee.tg_employee_lastname
            employee.tg_employee_surname = employee.tg_employee_surname
            employee.tg_employee_work_area = request.POST.get(
                'tg_employee_work_area')
            employee.tg_employee_birthday = employee.tg_employee_birthday
            employee.tg_employee_birthplace = request.POST.get(
                'tg_employee_birthplace')
            employee.tg_employee_phone = request.POST.get('tg_employee_phone')
            employee.tg_employee_city = request.POST.get('tg_employee_city')
            employee.tg_employee_distric = request.POST.get(
                'tg_employee_distric')
            employee.tg_employee_update = timezone.now()
            employee.tg_social_security = Tg_social_security.objects.get(
                pk=request.POST.get('tg_social_security'))
            employee.tg_employee_id_type = request.POST.get(
                'tg_employee_id_type')
            employee.tg_employee_id = employee.tg_employee_id
            employee.tg_employee_email = request.POST.get('tg_employee_email')
            employee.tg_employee_gender = request.POST.get(
                'tg_employee_gender')
            employee.tg_employee_address = request.POST.get(
                'tg_employee_address')
            employee.save()
            return redirect('/')

    except Exception as e:
        return e

    return render(request, 'employee_update.html', context)
