from django.shortcuts import render,HttpResponse,redirect
from loginapp import models
# Create your views here.
def login(request):
    err_msg = ''
    if request.method == 'POST':
        name_login = request.POST.get('name')
        pwd_login = request.POST.get('pwd')
        user_inDB = models.User.objects.filter(name=name_login).first()

        if not user_inDB:
            err_msg='无此用户'
        elif user_inDB.password == pwd_login:
            return redirect('/user_list/')
        else:
            err_msg='密码错误'

    return render(request,'login.html',{'error_message':err_msg})

def user_list(request):
    all_user = models.User.objects.all()
    return render (request,'user_list.html',{'user_list':all_user})

def add_user(request):
    if request.method == 'POST':
        new_name = request.POST.get('name')
        new_pwd = request.POST.get('pwd')
        models.User.objects.create(name=new_name,password=new_pwd)
        return redirect('/user_list/')
        

def del_user(request):
    del_id = request.GET.get('id')
    del_user = models.User.objects.filter(id=del_id)
    del_user.delete()
    return redirect('/user_list/')

def edit_user(request):
    if request.method == 'GET':
        get_id = request.GET.get('id')
        user = models.User.objects.get(id=get_id)
        return render(request,'edit_user.html',{'user':user})
    if request.method == 'POST':
        edit_id = request.POST.get('id')
        old_user = models.User.objects.get(id=edit_id)
        new_name = request.POST.get('name')
        new_pwd = request.POST.get('pwd')
        old_user.name = new_name
        old_user.password = new_pwd
        old_user.save()
        return redirect('/user_list/')
    

            



        
