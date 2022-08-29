""" This file contain all logical functionality on employees """
from django.shortcuts import render, HttpResponse,redirect
from django.views import View
from .models import Employee
from django.contrib import messages


class IndexView(View):
    """
    - This class contain the functionality of loading index page and creating new employee
    """
    def get(self,request):
        """
        - This function fetch all employee data and display on page
        - also shows the form for creating new employee entry
        """
        try:
            all_emp = Employee.objects.all()[::-1]
            context = {'all_emp' : all_emp}
            return render(request,'index_page/index.html',context)
        except Exception as e:
            return HttpResponse(e)
    def post(self,request):
        """
        - This function is responsible for creating new employee
        """
        try:
            name = request.POST['name']
            mobile = request.POST['mobile']
            address = request.POST['address']
            Employee.objects.create(name=name,mobile=mobile,address=address)
            all_emp = Employee.objects.all()[::-1]
            context = {'all_emp' : all_emp}
            messages.success(request,'Emploeyee saved successfully ... ')  
            return redirect('/')
        except Exception as e:
            return HttpResponse(e)


def DeleteEmployee(request,emp_id):
    """
    - This function is responsible for deleting employee
    """
    try:
        emp = Employee.objects.get(id = emp_id)
        emp.delete()
        messages.error(request,"Employee Deleted successfully ...")
        return redirect('/')
    except Exception as e:
            return HttpResponse(e)


class EditEmployeeView(View):
    """
    - This class is responsible to edit functionality on employees
    """
    def get(self,request,emp_id):
        """
        - This function shows all employee list and show the update employee form
        """
        try:
            sel_emp = Employee.objects.get(id = emp_id)
            all_emp = Employee.objects.all()[::-1]
            context = {
                'sel_emp' : sel_emp,
                'all_emp' : all_emp
            }
            return render(request,'index_page/index.html',context)
        except Exception as e:
            return HttpResponse(e)

    def post(self,request,emp_id):
        """
        - This function is responsible for updating employee's details
        """
        try:
            emp = Employee.objects.get(id = emp_id)
            emp.mobile = request.POST['mobile']
            emp.address = request.POST['address']
            emp.name = request.POST['name']
            emp.save()
            messages.success(request,"empoyee Updated successfully ...")
            return redirect('edit_emp',emp_id)
        except Exception as e:
            return HttpResponse(e)
