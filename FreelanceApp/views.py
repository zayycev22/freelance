import re
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Task , UserInfo
from django.contrib.auth.forms import PasswordChangeForm
import datetime
from django.contrib.auth import update_session_auth_hash
from django.test import TestCase,Client
"""
class IndexTest(TestCase):
    fixtures = ['test_database.json']
    def setUp(self):
        settings.configure()
        self.client=Client()

    def index_test(self):
        response= self.client.get('/')
        self.assertEqual(response.status_code,200)
"""
class Color:
    black = '\033[90m'
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[93m'
    blue = '\033[94m'
    purple = '\033[95m'
    cyan = '\033[96m'
    end = '\033[0m'

    # Пример использования цветов Color.green + "text" + Color.end


def home(request):
    return render(request, 'index.html')


def registration(request):
    return render(request, 'registration.html')


# Проверка введеных при регистрации данных (!пока частичная!)
def is_valid_form(first_name="Имя", second_name="Фамилия", password="Aa1234567890", email="email@test.com", username="testuserzero"):
    user_first_name_check = bool(re.search(r'[А-Я]{1}[а-я]+', first_name))
    user_last_name_check = bool(re.search(r'[А-Я]{1}[а-я]+', second_name))
    pass_check = bool(re.search(r'^(\w+\d+|\d+\w+)+$', password))
    email_check=bool(re.search(r'[\w.-]+@[\w.-]+', email))

    # login_check=re.search(r'[A-Za-z0-9]')
    print("email=", email_check, "имя фамилия=", user_first_name_check, user_last_name_check, "pass=", pass_check, len(password))
    if not User.objects.filter(username=username).exists() and user_first_name_check is True and \
            user_last_name_check is True and len(password) >= 8 and email_check and pass_check is True:
        return True
    else:
        return False


def create_user(request):
    if request.method == 'POST':
        if is_valid_form(request.POST.get("first_name"), request.POST.get("second_name"), request.POST.get("password"), request.POST.get("email"), request.POST.get('username')):
            user = User(username=request.POST.get('username'), email=request.POST.get("email"),
                        password=make_password(request.POST.get("password")),
                        first_name=request.POST.get("first_name"), last_name=request.POST.get("second_name"))

            # make_password() - создание хэша пароля
            user.save()
            text=request.POST.get('description')
            if text != None:
                info = UserInfo(text=text , userid=user.pk)
            else:
                info = UserInfo(userid=text)
            info.save()

            print(Color.blue + "Registration complite" + Color.end)
            return HttpResponseRedirect("/")
        else:
            print(Color.yellow + "Invalid form" + Color.end)
            return HttpResponseRedirect("/registration")
    else:
        print("HUGE PROBLEM")
        raise Http404


def edit_info(request):
    return render(request, 'edit_user.html')


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password, "try to log in")
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)

        else:
            print("Auth problems ...")
        return redirect("/")

    else:
        print("HUGE PROBLEM")
        raise Http404

    print(username, "logged in")
    return redirect('/')


def logout_page(request):
    logout(request)
    return redirect('/')


def top(request):
    user_list = User.objects.all()
    return render(request, 'top_list.html', {"users": user_list})


def all_tasks(request):
    u = request.user
    choice = request.POST.getlist('find[]')
    tasks = []
    tasks2 = []

    min_cost = request.POST.get("min_cost")
    max_cost = request.POST.get("max_cost")
    if min_cost==None:
        min_cost=0
    if max_cost==None:
        max_cost= 99999
    if min_cost=='':
        min_cost=0
    if max_cost=='':
        max_cost=99999999
    min_cost=float(min_cost)
    max_cost=float(max_cost)
    print(choice)
    print(min_cost)
    print(max_cost)
    if len(choice) > 0:
        for type in choice:
            cena = Task.objects.filter(type=type)
            print(cena)
            for task in cena:
                print(task)
                if task.cost >= min_cost and task.cost <= max_cost:
                    tasks += Task.objects.filter(pk=task.id)
        return render(request, 'tasks.html', {"tasks": tasks, "tasks2": tasks2, "icons": "icons/",
                                              "name": "My tasks", "action_url": "all_tasks"})
    else:
        cena = Task.objects.all()
        print(cena)
        for task in cena:
            print(task)
            if task.cost >=min_cost and task.cost <=max_cost:
                tasks+=Task.objects.filter(pk=task.id)
        return render(request, 'tasks.html', {"tasks": tasks, "tasks2": tasks2, "icons": "icons/",
                                              "name": "My tasks", "action_url": "all_tasks"})


@login_required()
def new_task(request):
    return render(request, "new_task.html")


def my_tasks(request):
    u = request.user
    choice = request.POST.getlist('find[]')
    tasks = []
    tasks2 = []
    min_cost = request.POST.get("min_cost")
    max_cost = request.POST.get("max_cost")
    if min_cost == None:
        min_cost = 0
    if max_cost == None:
        max_cost = 99999
    if min_cost == '':
        min_cost = 0
    if max_cost == '':
        max_cost = 99999999
    min_cost = float(min_cost)
    max_cost = float(max_cost)
    print(choice)
    print(min_cost)
    print(max_cost)
    if len(choice) > 0:
        for type in choice:
            cena = Task.objects.filter(create_user_id=u.pk, type=type)
            cena2 = Task.objects.filter(submit_user_id=u.pk, type=type)
            print(cena)
            for task in cena:
                print(task)
                if task.cost >= min_cost and task.cost <= max_cost:
                    tasks += Task.objects.filter(pk=task.id)
            for task in cena2:
                print(task)
                if task.cost >= min_cost and task.cost <= max_cost:
                    tasks2 += Task.objects.filter(pk=task.id)

        return render(request, 'tasks.html', {"tasks": tasks, "tasks2": tasks2, "icons": "icons/",
                                          "name": "My tasks", "action_url": "my_tasks"})

    else:
        cena = Task.objects.filter(create_user_id=u.pk)
        cena2 = Task.objects.filter(submit_user_id=u.pk)
        print(cena)
        for task in cena:
            print(task)
            if task.cost >= min_cost and task.cost <= max_cost:
                tasks += Task.objects.filter(pk=task.id)
        for task in cena2:
            print(task)
            if task.cost >= min_cost and task.cost <= max_cost:
                tasks += Task.objects.filter(pk=task.id)

        return render(request, 'tasks.html', {"tasks": tasks, "tasks2": tasks2, "icons": "icons/",
                                          "name": "My tasks", "action_url": "my_tasks"})


def task_info(request, id):
    task = Task.objects.get(id=id)
    user_id = User.objects.get(username=task.name).id
    return render(request, 'task_info_page.html', {"task": task, "icons": "icons/", "user_id": user_id})


def create_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        cost = request.POST.get("cost")

        statu = "Открыто"
        tupe = request.POST.get('type')
        dat = datetime.datetime.now()
        user_create_task=request.user
        print(title, description, cost, statu,tupe ,"try to create")
        task = Task(title=title, text=description, cost=cost, name=request.user.username, status=statu, type=tupe,date=dat,create_user_id=user_create_task.id)
        task.save()
        return redirect('/')
    else:
        print("HUGE PROBLEM")
        raise Http404

def my_info(request):
    user_info = request.user
    info = UserInfo.objects.get(userid=user_info.pk)
    return render(request, 'user_info.html', {"info": info, "user_info": user_info})


def user_info(request, id):
    user_info = User.objects.get(id=id)
    info = UserInfo.objects.get(userid=user_info.id)
    return render(request, 'user_info.html', {"info": info, "user_info": user_info})


def change_info(request):
    u = request.user
    info = UserInfo.objects.get(id=u.pk)
    if request.method=='POST':
        text = request.POST.get('text')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        u = request.user
        info=UserInfo.objects.get(userid=u.pk)
        if text != None:
            info.text = text
            info.save()
        if name != None:
            u.first_name=name
            u.save()
        if surname != None:
            u.last_name = surname
            u.save()
        if username != None:
            u.username = username
            u.save()
        if email != None:
            u.email = email
            u.save()

        return HttpResponseRedirect("/user/info")
    return render(request, 'change_info.html', {"info": info})


def change_pass(request):
    u = User.objects.get(username=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)
        old_pass = (request.POST.get("old_pass"))
        new_pass = (request.POST.get("new_pass"))
        if u.check_password(old_pass) and is_valid_form(password=new_pass):
            u.password=make_password(new_pass)
            u.save()
            print("ok")
            return HttpResponseRedirect("/")
        else:
            print("not ok")
    else:
        form = PasswordChangeForm(u)

    return render(request, 'change_pass.html',
                  {'form': form, 'user': u})


def delete_task(request, id):
    u=request.user

    task = Task.objects.filter(id=id)[0]
    print(u.id,task.create_user_id)
    if request.method == 'POST':
        if u.id == task.create_user_id:
            if task.status == "Открыто":
                task.delete()
                return HttpResponseRedirect("/my_tasks")

            else:
                print(Color.blue + "Not open status" + Color.end)
                return HttpResponseRedirect("/task/" + str(task.id))
        return HttpResponseRedirect("/")
    else:
        print(Color.blue + "Error" + Color.end)
        return HttpResponseRedirect("/my_tasks")


def change_status(request, id):
    task = Task.objects.filter(id=id)[0]
    u=request.user
    status = request.POST.get('status')
    print(status)

    if status == 'take':
        print(Color.blue + "Open -> In progress" + Color.end)
        print(u)
        task.status = "В процессе"
        task.submit_user_id=u.pk
        task.save()
        return HttpResponseRedirect("/my_tasks")
    elif status == 'deny':
        print(Color.purple + "Open <- In progress" + Color.end)
        print(u)
        task.status = "Открыто"
        task.submit_user_id = 0
        task.save()
        return HttpResponseRedirect("/my_tasks")
    elif status == 'complete':
        print(Color.blue + "In progress -> Complete" + Color.end)
        print(u)
        task.status = "Выполнена"
        task.save()
        return HttpResponseRedirect("/my_tasks")
    else:
        print(Color.red + "Error" + Color.end)
        return HttpResponseRedirect("/my_tasks")
