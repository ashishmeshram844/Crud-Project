from django.shortcuts import render, HttpResponse,redirect
from django.views import View
from .models import Employee
from django.contrib import messages


class IndexView(View):
    def get(self,request):
        try:
            all_emp = Employee.objects.all()[::-1]
            context = {'all_emp' : all_emp}
            return render(request,'index_page/index.html',context)
        except Exception as e:
            return HttpResponse(e)
    def post(self,request):
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
    try:
        emp = Employee.objects.get(id = emp_id)
        emp.delete()
        messages.error(request,"Employee Deleted successfully ...")
        return redirect('/')
    except Exception as e:
            return HttpResponse(e)


class EditEmployeeView(View):
    def get(self,request,emp_id):
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