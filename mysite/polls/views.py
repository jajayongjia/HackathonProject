from django.http import HttpResponse
from  .models import Ranking
import json
from django.views.decorators.csrf import csrf_exempt
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
        data = {"yearRange": [], 'location':[],'studentType':[]}
        yearRange = Ranking.objects.distinct().order_by().values('yearRange')
        location = Ranking.objects.distinct().order_by().values('location')
        studentType = Ranking.objects.distinct().order_by().values('studentType')
        for i in yearRange:
            data['yearRange'].append(i['yearRange'])
        for j in location:
            data['location'].append(j['location'])
        for j in studentType:
            data['studentType'].append(j['studentType'])
        return HttpResponse(status=200, content=json.dumps(data), content_type='application/json')
    else:
        return HttpResponse(status=405)


@csrf_exempt
@api_view(['POST'])
def getTuitionForTwoLocation(request):
    if request.method=='POST':
        data = {"data": []}
        qs = Ranking.objects.filter(Q(location=request.POST.get('location1'), yearRange=request.POST.get("yearRange")) |
                                    Q(location=request.POST.get('location2'), yearRange=request.POST.get("yearRange"))
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

