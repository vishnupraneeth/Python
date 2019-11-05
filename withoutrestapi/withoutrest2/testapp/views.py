from django.shortcuts import render
from testapp.models import Employee
from django.views.generic import View
from django.core.serializers import serialize
from django.http import HttpResponse
from testapp.mixins import HttpResponseMixin,SerializeMixin
# Create your views here.
import json
class EmployeeCBV(SerializeMixin,HttpResponseMixin,View):
    def get(self,request,id,*args,**kwargs):
        try:
            qs=Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data=json.dumps({'msg':'The required data does not exist'})
            return self.render_to_http_response(json_data,status=404)
        else:
            json_data=self.serialize([qs,])
            return self.render_to_http_response(json_data)

class EmployeeCBVall(SerializeMixin,View):
    def get(self,request,*args,**kwargs):
        qset=Employee.objects.all()
        p_data=self.serialize(qset)
        # j_data=serialize('json',qset)
        # lst=json.loads(j_data)
        # l=[]
        # for obj in lst:
        #     l.append(obj['fields'])
        # data=json.dumps(l)
        return HttpResponse(p_data,content_type='application/json')
