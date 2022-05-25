from django.contrib import admin
from django.urls import path
from task1 import views 

urlpatterns = [
    path("",views.Listtask1APIView.as_view(),name="task1_list"),
    path("create/", views.Createtask1APIView.as_view(),name="task1_create"),
    path("update/<int:pk>/",views.Updatetask1APIView.as_view(),name="update_task1"),
    path("delete/<int:pk>/",views.Deletetask1APIView.as_view(),name="delete_task1")
]