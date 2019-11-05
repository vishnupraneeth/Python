
from django.http import HttpResponse
import json
from django.core.serializers import serialize
class SerializeMixin(object):
    def serialize(self,qs):
        j_data=serialize('json',qs)
        lst=json.loads(j_data)
        l=[]
        for obj in lst:
            l.append(obj['fields'])
        data=json.dumps(l)
        return data

class HttpResponseMixin(object):
    def render_to_http_response(self,json_data,status=200):
        return HttpResponse(json_data,content_type="application/json",status=status)
