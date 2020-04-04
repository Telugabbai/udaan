from django.shortcuts import render,redirect
from employee.models import  Employee
from employee import forms


# Create your views here.

def index(request):
    return  render(request,'home.html')

def display_emp(request):
    emp = Employee.objects.all()
    return  render(request,"display.html",{'employee':emp})

def create_emp(request):
    if request.method == 'GET':
        return render(request,'create.html')
    elif request.method == 'POST':
        emp_name = request.POST['name']
        phone = request.POST['phone']
        salary = request.POST['salary']
        city = request.POST['city']
        dept = request.POST['dept']
        Employee(emp_name=emp_name,phone=phone,salary=salary,city=city,dept=dept).save()
        return render(request,'create.html',{'status':'Data insert successfully'})


def update_emp(request,id):
    obj = Employee.objects.get(id=id)
    if request.method == 'GET':
        return render(request,'update.html',{'emp':obj})
    elif request.method == 'POST':
        obj.emp_name = request.POST['name']
        obj.phone = request.POST['phone']
        obj.salary = request.POST['salary']
        obj.city = request.POST['city']
        obj.dept = request.POST['dept']
        obj.save()
        return redirect('display')


def delete_emp(request,id):
    em=Employee.objects.get(id=id)
    em.delete()
    return redirect('display')



def thankyou(request):
    return render(request,'thankyou.html')

def feedback(request):
    form = forms.FeedbackForm()
    if request.method == 'post':
        form = forms.FeedbackForm(request.post)
        if form.is_valid():
            print('validation completed ')
            print('Employee Name :',form.cleaned_data['name'])
            print('Employee Number :', form.cleaned_data['empno'])
            print('Employee Emailid :', form.cleaned_data['emailid'])
            print('Employee Feedback :', form.cleaned_data['feedback'])
            return thankyou(request)
        return render(request,'feedback.htm',{'form':form})


