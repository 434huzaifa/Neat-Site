from django.shortcuts import render, redirect
from . import models
from django.shortcuts import render, HttpResponse
from . import forms
from django.contrib.auth.models import Group, User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.http import JsonResponse
from datetime import datetime, timedelta
#from django.core.exceptions import ObjectDoesNotExist
# Create your views here.



def t(request):
    
    return render(request, 't.html', context)


@unauthenticated_user
def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me',False)
        print(remember_me)
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            if not remember_me:
                request.session.set_expiry(0)    
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group == 'Client':
                return redirect('salons')
            else:
                return redirect('SalonOwner')
        else:
            messages.error(request, "The Password and Username Mismatch")

    return render(request, 'login.html')


@login_required(login_url='home')
def logoutUser(request):
    logout(request)
    return redirect('/')


@login_required(login_url='home')
@allowed_users(['Client'])
def salons(request):
    salons = models.salon.objects.all()
    context={
        'salons': salons,
    }
    return render(request, 'salon.html',context)


@unauthenticated_user
def salonReg(request):
    Userform = forms.CreateUserForm()
    Salonform = forms.CreateSalon()
    if request.method == "POST":
        Userform = forms.CreateUserForm(request.POST)
        if Userform.is_valid():
            Salonform = forms.CreateSalon(request.POST)

            if Salonform.is_valid():
                user = Userform.save()
                salon = Salonform.save(commit=False)
                salon.sal_user = user
                myr_group = Group.objects.get_or_create(name='Salon')
                my_group = Group.objects.get(name='Salon')
                my_group.user_set.add(user)
     
                Salonform.save()
                return redirect('/')
            else:
                print(Salonform.data)
                messages.error(request, Salonform.errors)
                print(Salonform.errors.as_text())
        else:
            print(Userform.data)
            messages.error(request, Userform.errors)
            print(Userform.errors.as_text())

    context = {'Userform': Userform,
               'Salonform': Salonform}

    return render(request, 'salonReg.html', context)


@unauthenticated_user
def clientReg(request):
    Userform = forms.CreateUserForm()
    Cleintform = forms.CreateCleint()
    if request.method == "POST":
        Userform = forms.CreateUserForm(request.POST)
        Cleintform = forms.CreateCleint(request.POST)
        if Userform.is_valid():
            if Cleintform.is_valid():
                user = Userform.save()
                client = Cleintform.save(commit=False)
                client.cl_user = user
                Cleintform.save()
                myr_group = Group.objects.get_or_create(name='Client')
                my_group = Group.objects.get(name='Client')
                my_group.user_set.add(user)
                return redirect('/')
            else:
                print(Cleintform.data)
                print(Cleintform.errors.as_text())
                messages.error(request, Cleintform.errors)
        else:
            print(Userform.data)
            print(Userform.errors.as_data())
            messages.error(request, Userform.errors)

    context = {'Userform': Userform,
               'Cleintform': Cleintform}

    return render(request, 'clientReg.html', context)

#what will happen if the appointment succeed

@login_required(login_url='home')
def sinlgeSalonView(request, id):
    client=models.client.objects.get(cl_user=request.user)
    salon = models.salon.objects.get(id=id)
    appoint=models.apointment.objects.all().filter(a_client=client,a_salon=salon)
    cart=models.cart.objects.all().filter(c_client=client,c_salon=salon)
    services = models.services.objects.all().filter(s_salon=salon)
    ch=[]
    cart_ch=[]
    if appoint:
        appoint=appoint.get(a_client=client,a_salon=salon)
        for i in appoint.a_service.all():
            services=services.exclude(id=i.id)
            ch.append(str(i.id))
    if cart:
        cart=cart.get(c_client=client,c_salon=salon)
        for i in cart.c_service.all():
            services=services.exclude(id=i.id)
            ch.append(str(i.id))
    
    appoint_salon=models.apointment.objects.all().filter(a_salon=salon)

    wait_time=0
    t_hour=0
    t_min=0
    for s in appoint_salon:
        if s.a_client==client:
            break
       
    print(appoint)
    context = {
        'salon': salon,
        'services': services,
        'appoint': appoint,
        'cart': cart,
        'wait_time': wait_time,
    }

    return render(request, 'singlesalon.html',context)



@login_required(login_url='home')
@allowed_users(['Salon'])
def salonOwner(request):
    salon = request.user.salon
    services = models.services.objects.all().filter(s_salon=salon)
    appoints=models.apointment.objects.all().filter(a_salon=salon)
    print(services)
    context = {
        'services': services,
        'appoints': appoints
    }
    return render(request, 'salonOwner.html', context)

@login_required(login_url='home')
@allowed_users(['Salon'])
def update_status(request):
    Id=request.POST['id']
    status=request.POST['action']
    appoint=models.apointment.objects.get(id=Id)
    if status=='1':
        appoint.a_status='Accept'
        appoint.save()
        app=models.apointment.objects.all().filter(a_status="Accept")
        app_list=list()
        for i in app:
            app_dict=dict()
            app_dict['id']=i.id
            app_dict['name']=i.a_client.cl_name
            ser=""
            for j in i.a_service.all():
                ser+=j.s_name+","
            app_dict['services']=ser
            app_list.append(app_dict)
        return JsonResponse({'status':1,'appoint':app_list})
    elif status=='2':
       appoint.delete()
       return JsonResponse({'status':2})
    elif status=='3':
        appoint.delete()
        return JsonResponse({'status':3})
    elif status=='4':
        appoint.delete()
        return JsonResponse({'status':4})
    
    return JsonResponse({'status':0})


@login_required(login_url='home')
@allowed_users(['Salon'])
def service(request):
    Serviceform = forms.CreateService()
    if request.method == "POST":
        Serviceform = forms.CreateService(request.POST)
        if Serviceform.is_valid():
            s = Serviceform.save(commit=False)
            salon = request.user.salon
            s.s_salon = salon
            Serviceform.save()
            return redirect('SalonOwner')
        else:
            messages.error(Serviceform.errors)
    context = {
        'Serviceform': Serviceform
    }
    return render(request, 'service.html', context)


@login_required(login_url='home')
@allowed_users(['Client'])
def deleteAppointmentServices(request):
    if request.method=='POST':
        cart_id=request.POST['cartid']
        idd=request.POST['id']
        print(models.cart.objects.count())
        cart=models.cart.objects.get(id=cart_id)
        ser=models.services.objects.get(id=idd)
        serv_list=""
        salon=models.salon.objects.get(id=cart.c_salon.id)
        client=models.client.objects.get(cl_user=request.user)
        services = models.services.objects.all().filter(s_salon=salon)
        appoint=models.apointment.objects.all().filter(a_client=client,a_salon=salon)
        
        for i in cart.c_service.all():
            services=services.exclude(id=i.id)
        if appoint:
            appoint=appoint.get(a_client=client,a_salon=salon)
            for i in appoint.a_service.all():
                services=services.exclude(id=i.id)
        print(services)
        serv_list=list()
        for s in services:
            serv_dict=dict()
            serv_dict['id']=s.id
            serv_dict['name']=s.s_name
            serv_dict['price']=s.s_price
            serv_dict['hour']=s.s_ehour
            serv_dict['min']=s.s_emin
            serv_dict['about']=s.s_about
            serv_list.append(serv_dict)
        st=cart.c_service.remove(ser)
        if cart.c_service.count()==0:
            cart.delete()
        return JsonResponse({'status':1,'serv':serv_list})
    return JsonResponse({'status':0})



def delete_service(request):
    sId=request.POST['id']
    s=models.services.objects.get(id=sId)
    s.delete()
    return JsonResponse({'status':1})


def search_salon(request):
    keyword=request.POST['keyword']
    salon=models.salon.objects.values().filter(sal_name__icontains=keyword)
    if len(salon)!=0:
        salon_list=list(salon)
        print(salon_list)
        return JsonResponse({'status':1,'salon':salon_list})
    else:
        return JsonResponse({'status':0})
    
def reset_search(request):
    salon=models.salon.objects.values()
    print(salon)
    if len(salon)!=0:
        salon_list=list(salon)
        print(salon_list)
        return JsonResponse({'status':1,'salon':salon_list})
    else:
        return JsonResponse({'status':0})
    
def service_cart(request):
    if request.method=='POST':
        checklist=request.POST.getlist('checks[]')
        iid=request.POST['id']
        client=models.client.objects.get(cl_user=request.user)
        salon = models.salon.objects.get(id=iid)
        services = models.services.objects.all().filter(s_salon=salon)
        cart= models.cart.objects.all().filter(c_client=client,c_salon=salon)
        cart_id=0
        cart_checks=[]
        
        if cart.count()!=0:
            cart=cart.get(c_client=client,c_salon=salon)
            cart_id=cart.id
            for serv in cart.c_service.all():
                cart_checks.append(serv.id)
        
        if checklist !=[]:
            if cart_checks !=[]:
                for i in checklist:
                    cart_checks.append(i)
                checklist=cart_checks

            cart_list=list()
            t_hour=0
            t_min=0
            total_price=0.0
            for service in services:
                cart_dict=dict()
                for check in checklist:
                    if check==str(service.id):
                        cart_dict['id']=service.id
                        cart_dict['name']=service.s_name
                        cart_dict['price']=service.s_price
                        cart_dict['hour']=service.s_ehour
                        cart_dict['min']=service.s_emin
                        total_price+=service.s_price
                        t_hour+=service.s_ehour
                        t_min=+service.s_emin
                        cart_list.append(cart_dict)
            t_time=time_convert(t_hour, t_min)
            if cart_id !=0:
                obj=models.cart(id=cart_id,c_client=client,c_salon=salon)
            else:
                obj=models.cart(c_client=client,c_salon=salon)
            obj.save()
            obj.c_service.set(checklist)
            return JsonResponse({'status':1,'cart':cart_list,'cart_id':obj.id})
        return JsonResponse({'status':2})
    return JsonResponse({'status':0})

def time_convert(h,m):
    now = datetime.now()
    time_change = timedelta(hours=h,minutes=m)
    new_time = now + time_change
    print(str(new_time))
    return str(new_time)
    
def make_appoint(request):
    if request.method=='POST':
        idd=request.POST['cartid']
        print(idd)
        cart=models.cart.objects.get(id=idd)
        services=models.services.objects.all().filter(s_salon=cart.c_salon)
        print(cart)
        total_price=0.0
        t_hour=0
        t_min=0
        serv_list=list()
        for serv in services:
            for s in cart.c_service.all():
                if s.id == serv.id:
                    serv_dict=dict()
                    serv_dict['name']=serv.s_name
                    serv_dict['price']=serv.s_price
                    serv_dict['hour']=serv.s_ehour
                    serv_dict['min']=serv.s_emin
                    serv_list.append(serv_dict)
                    total_price+=serv.s_price
                    t_hour+=serv.s_ehour
                    t_min+=serv.s_emin
        if t_min>59:
            t_hour+=int(t_min/60)
            t_min-=int((t_min/60))*60
        obj=models.apointment(a_client=cart.c_client,a_salon=cart.c_salon,a_total_price=total_price,a_ehour=t_hour,a_emin=t_min)
        obj.save()
        obj.a_service.set(cart.c_service.all())
        print(total_price)           
        cart.delete()
        return JsonResponse({'status':1,'service':serv_list,'hour':t_hour,'min':t_min,'price':total_price})
    return JsonResponse({'status':0})

