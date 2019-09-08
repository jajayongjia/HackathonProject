from django.http import HttpResponse
from  .models import Ranking
import json
from django.db.models import Q
def get_all_data(request):
    if request.method == 'GET':
        data = {"data": []}
        qs = Ranking.objects.all()
        for one_rank in qs:
            data['data'].append({
                "id": one_rank.id,
                "year": one_rank.yearRange,
                "location": one_rank.location,
                "type": one_rank.studentType,
                "tuition": one_rank.tuitionFee
                })
        return HttpResponse(status=200, content=json.dumps(data), content_type='application/json')
    else:
        return HttpResponse(status=405)

def getDistinctValue(request):
    if request.method=='GET':
        data = {"yearRange": [], 'location':[]}
        yearRange = Ranking.objects.distinct().order_by().values('yearRange')
        location = Ranking.objects.distinct().order_by().values('location')
        for i in yearRange:
            data['yearRange'].append(i['yearRange'])
        for j in location:
            data['location'].append(j['location'])
        return HttpResponse(status=200, content=json.dumps(data), content_type='application/json')
    else:
        return HttpResponse(status=405)

def getTuitionForTwoLocation(request):
    if request.method=='GET':
        data = {"data": []}

        qs = Ranking.objects.filter(Q(location=request.GET('location1'), yearRange=request.GET("yearRange")) |
                                    Q(location=request.GET('location2'), yearRange=request.GET("yearRange"))
                                    )

        for one_rank in qs:
            data['data'].append({
                "id": one_rank.id,
                "year": one_rank.yearRange,
                "location": one_rank.location,
                "type": one_rank.studentType,
                "tuition": one_rank.tuitionFee
                })
        return HttpResponse(status=200, content=json.dumps(data), content_type='application/json')
    else:
        return HttpResponse(status=405)
