from django.shortcuts import render
import datetime
from testApp.models import Employee
from . import forms 

# Create your views here.
def wish(request): 
	 return render(request,'testApp/wish.html') 

def wishone(request): 
	 date=datetime.datetime.now() 
	 my_dict={'insert_date':date} 
	 return render(request,'testApp/wish.html',context=my_dict)

def empdata(request):
	emp_list=Employee.objects.all() 
	my_dict={'emp_list':emp_list}   
	return render(request, 'testApp/emp.html', context=my_dict)   

def studentinputview(request): 
	 form=forms.StudentForm() 
	 if request.method=='POST':
	     form=forms.StudentForm(request.POST)
	      if form.is_valid(): 
	          print('Form validation success and printing data')   
	          print('Name:',form.cleaned_data['name']) 
	          print('Marks:',form.cleaned_data['marks'])     
return render(request,'testApp/input.html',{'form':form})  