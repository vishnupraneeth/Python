from django.shortcuts import render
from testapp.models import Employee
from django.views.generic import View
from django.core.serializers import serialize
from django.http import HttpResponse
import json
# Create your views here.
class EmployeeCBV(View):
    def get(self,request,id,*args,**kwargs):
        print("id==",id)
        qs=Employee.objects.get(id=id)
        json_data = serialize('json',[qs,])
        return HttpResponse(json_data,content_type='application/json')
class EmployeeCBVall(View):
    def get(self,request,*args,**kwargs):

        qs1=Employee.objects.all()
        json_data = serialize('json',qs1)
        p_data=json.loads(json_data)
        dummy_list=[]
        for obj in p_data:
           emp_data=obj['fields']
           dummy_list.append(emp_data)

        json_data=json.dumps(dummy_list)
        return HttpResponse(json_data,content_type='application/json')
