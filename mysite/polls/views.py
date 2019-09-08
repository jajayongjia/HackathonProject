from django.http import HttpResponse
from  .models import Ranking
import json

def get_all_data(request):
    if request.method == 'GET':
        data = {"data": []}
        qs = Ranking.objects.all()
        for one_rank in qs:
            data['data'].append({
                "id": one_rank.id,
                "yearRange": one_rank.yearRange,
                "localtion": one_rank.location,
                "studentType": one_rank.studentType,
                "tuitionFee": one_rank.tuitionFee
                })
        return HttpResponse(status=200, content=json.dumps(data), content_type='application/json')
    else:
        return HttpResponse(status=405)
