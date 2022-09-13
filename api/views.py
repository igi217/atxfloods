from django.http import JsonResponse
from admin.models import Crossing, Camera
from admin.helpers import Helpers
# Create your views here.


def crossings(request):
    crossings = Crossing.objects.order_by('id')
    crossings_json = Helpers.parse_crossings_json(crossings)
    return JsonResponse({'status': 200, 'message': 'Request Successfull!', 'totalResult': crossings.count(), 'attributes': crossings_json})


def closures(request):
    closures = Crossing.objects.filter(status=0).order_by('id')
    closures_json = Helpers.parse_crossings_json(closures)
    return JsonResponse({'status': 200, 'message': 'Request Successfull!', 'totalResult': closures.count(), 'attributes': closures_json})


def cameras(request):
    cameras = Camera.objects.order_by('id')

    camera_json = Helpers.parse_cameras_json(cameras)
    return JsonResponse({'status': 200, 'message': 'Request Successfull!','totalResult':cameras.count(), 'attributes': camera_json})
