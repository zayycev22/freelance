from django.urls import path,re_path,include
from django.conf import settings
from django.conf.urls.static import static
from FreelanceApp.views import *
from django.contrib import admin
from django.views.generic import TemplateView
from chat.views import *
from django.conf.urls import url
urlpatterns = [
    path('', home),
    path('registration', registration),
    path('user/login', login_page),
    path('user/logout', logout_page),
    path('top', top),
    path('user/registration', create_user),
    path('new_task', new_task),
    path('my_tasks', my_tasks),
    path('all_tasks', all_tasks),
    path('task/<int:id>', task_info),
    path('user/create_task', create_task),
    path('user/info', my_info),
    path('user/<int:id>', user_info),
    path('change_pass', change_pass),
    path('remove_task/<int:id>', delete_task),
    path('change_status/<int:id>', change_status),
    path('user/change_info', change_info),
    path('admin/', admin.site.urls),
    path('messages/', include('chat.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
