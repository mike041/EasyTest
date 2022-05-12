"""xsolla URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from base.views import *
from base.xsolla import *

urlpatterns = [
    path(r'xsolla/', xsolla),
    path(r'project/', project_index),
    path(r'project_add/', project_add),
    path(r'project_update/', project_update),
    path(r'project_delete/', project_delete),

    path(r'sign/', sign_index),
    path(r'sign_add/', sign_add),
    path(r'sign_update/', sign_update),

    path(r'env/', env_index),
    path(r'env_add/', env_add),
    path(r'env_update/', env_update),

    path(r'interface/', interface_index),
    path(r'interface_add/', interface_add),

    path(r'case/', case_index),
    path(r'case_add/', case_add),
    path(r'case_run/', case_run),

    path(r'plan/', plan_index),
    path(r'plan_add/', plan_add),
    path(r'plan_run/', plan_run),

    path(r'report/', report_index),

    path(r'findata/', findata)
]
