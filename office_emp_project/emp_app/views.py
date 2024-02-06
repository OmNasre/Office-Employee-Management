from django.shortcuts import render, HttpResponse, redirect
from .models import Employee,Department,Role 
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, "emp_app/index.html")

def view_emp(request):
    emps = Employee.objects.all()
    context = {
        "emps" : emps
    }
    return render(request, "emp_app/view_emp.html", context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        dept = request.POST.get("dept")
        salary = request.POST.get("salary")
        role = request.POST.get("role")
        phone = request.POST.get("phone")
        nps = Employee(first_name=first_name, last_name=last_name,dept_id=dept,salary=salary,role_id = role, phone=phone, hire_date = datetime.now())
        nps.save()
        return redirect("/view_emp")
        
    return render(request, "emp_app/add_emp.html")

def remove_emp(request):
    
    if request.method == "GET":
        fname = request.GET.get("fname")
        if fname!=None:
                final_data = Employee.objects.filter(first_name__icontains = fname)
                return render(request, "emp_app/remove_emp.html", {"emps" : final_data})
            
    return render(request, "emp_app/remove_emp.html")

def filter_emp(request):
    return render(request, "emp_app/filter_emp.html")

def remove_emp2(request, emp_id = 0):
    if emp_id != 0:
        try:
            emp_to_removed = Employee.objects.get(id = emp_id)
            emp_to_removed.delete()
            return redirect("/view_emp")
            

        except:
            pass
    
    