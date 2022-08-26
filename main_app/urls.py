from ast import Delete
from django.urls import path,include
from main_app.views import IndexView,DeleteEmployee,EditEmployeeView
urlpatterns = [
    path('',IndexView.as_view(),name="index"),
    path('delete_emp/<int:emp_id>/',DeleteEmployee,name="delete_emp"),
    path('edit_emp/<int:emp_id>/',EditEmployeeView.as_view(),name="edit_emp")
]