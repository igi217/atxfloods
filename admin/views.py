import json
import base64
from unicodedata import name
from django.contrib.postgres.search import SearchVector
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
from atxfloods.settings import MEDIA_ROOT
from .helpers import Helpers, auth, handle_csv_import
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Crossing, Camera, Image
from urllib.request import urlretrieve


@auth
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@auth
def count(request):
    crossing_count = Crossing.objects.count()
    closures_count = Crossing.objects.filter(status=0).count()
    camera_count = Camera.objects.count()

    return JsonResponse({'status': 200, 'data': {
        'totalCrossing': crossing_count,
        'totalClosures': closures_count,
        'totalCamera': camera_count
    }})


@csrf_exempt
def login(request):
    if request.method == 'GET':
        return Helpers.request_method_error('GET')
    credentials = json.loads(request.body.decode("utf-8"))
    user = authenticate(username=credentials['username'],
                        password=credentials['password'])
    if user is not None:
        # Token
        token = request.body.decode("utf-8")
        token_bytes = token.encode('ascii')
        base64_bytes = base64.b64encode(token_bytes)
        _token = base64_bytes.decode('ascii')

        # Response Body
        response_body = {}
        response_body['status'] = 200
        response_body['message'] = 'Authentication Successfull'
        response_body['_token'] = _token

        return JsonResponse(response_body)
    # Auth failed
    response_body = {}
    response_body['status'] = 500
    response_body['message'] = 'Authentication Failed'

    return JsonResponse(response_body)


@csrf_exempt
@auth
def change_password(request):
    if request.method == 'GET':
        return Helpers.request_method_error('GET')
    credentials = request.user
    request_body = json.loads(request.body.decode("utf-8"))
    users = User.objects.filter(id=credentials.id)

    # you can user username or etc to get users query set
    # you can also use get method to get users
    user = users[0]
    user.set_password(request_body['password'])
    user.save()
    # Creqting New Token
    new_credentials = {'username': request.user.username,
                       'password': request_body['password']}
    json_encoded = json.dumps(new_credentials)

    token_bytes = json_encoded.encode('ascii')
    base64_bytes = base64.b64encode(token_bytes)
    _token = base64_bytes.decode('ascii')

    # Response Body
    response_body = {}
    response_body['status'] = 200
    response_body['message'] = 'Crdentials Changed!'
    response_body['_token'] = _token

    return JsonResponse(response_body)


@csrf_exempt
@auth
def all_crossings(request):
    per_page = request.GET.get('per_page') or 10
    page_number = request.GET.get('page_number') or 1
    status = request.GET.get('status')
    search = request.GET.get('search')
    if not status and not search:
        crossings = Crossing.objects.order_by('id')
    elif status and not search:
        crossings = Crossing.objects.filter(status=int(status)).order_by('id')
    elif status and search:
        crossings = Crossing.objects.annotate.filter(Q(name__icontains=search) | Q(address__icontains=search) & Q(status=int(status))).order_by('id')
    elif not status and search:
        crossings = Crossing.objects.filter(Q(name__icontains=search) | Q(address__icontains=search)).order_by('id')
    paginator = Paginator(crossings, per_page)
    page_obj = paginator.get_page(page_number)
    crossings_json = Helpers.parse_crossings_json(page_obj)

    return JsonResponse({'total': crossings.count(), 'status': 200, 'data': crossings_json}, safe=False)


@csrf_exempt
@auth
def create_crossing(request):
    if request.method == 'GET':
        return Helpers.request_method_error('GET')
    request_body = json.loads(request.body.decode("utf-8"))
    crossing = Crossing(
        name=request_body['name'],
        jurisdiction=request_body['jurisdiction'],
        address=request_body['address'],
        lat=request_body['lat'],
        lon=request_body['lon'],
        comment=request_body['comment'],
        status=request_body['status'],

    )
    crossing.save()

    return JsonResponse({'status': 200, 'message': 'New Crossing Created'})


@csrf_exempt
@auth
def update_crossing(request, id):
    if request.method == 'GET':
        return Helpers.request_method_error('GET')
    request_body = json.loads(request.body.decode("utf-8"))
    crossing = Crossing.objects.get(id=id)
    crossing.name = request_body['name']
    crossing.jurisdiction = request_body['jurisdiction']
    crossing.address = request_body['address']
    crossing.lat = request_body['lat']
    crossing.lon = request_body['lon']
    crossing.comment = request_body['comment']
    crossing.status = request_body['status']
    crossing.save()

    return JsonResponse({'status': 200, 'message': 'New Crossing Created'})


@auth
def delete_crossing(request, id):
    if id is None:
        return JsonResponse({'status': 500, 'message': 'Id is required'})
    crossing = Crossing(id=id)
    crossing.delete()

    return JsonResponse({'status': 200, 'message': 'Record Deleted'})


@csrf_exempt
@auth
def import_crossing(request):
    if request.method == 'GET':
        return Helpers.request_method_error('GET')
    if not request.FILES['file']:
        return JsonResponse({'status': 500, 'message': 'File is not available in Request'})
    file = request.FILES['file']
    response_data = handle_csv_import(file)
    return JsonResponse({'status': 200, 'data': response_data}, safe=False)


@auth
def closures(request):
    closures = Crossing.objects.filter(status=0).order_by('id')
    per_page = request.GET.get('per_page') or 10
    page_number = request.GET.get('page_number') or 1

    paginator = Paginator(closures, per_page)
    page_obj = paginator.get_page(page_number)

    closures_json = Helpers.parse_crossings_json(page_obj)

    return JsonResponse({'total': closures.count(), 'status': 200, 'data': closures_json}, safe=False)


@auth
def cameras(request):
    cameras = Camera.objects.order_by('id')
    per_page = request.GET.get('per_page') or cameras.count()
    page_number = request.GET.get('page_number') or 1

    paginator = Paginator(cameras, per_page)
    page_obj = paginator.get_page(page_number)
    camera_json = Helpers.parse_cameras_json(page_obj)
    return JsonResponse({'status': 200, 'message': 'Request Successfull!', 'totalResult': cameras.count(), 'attributes': camera_json})

@csrf_exempt
@auth
def camera_single(request, id):
    if request.method == 'GET':
        return Helpers.request_method_error('GET')
    camera = Camera.objects.filter(id = id)
    camera_json = Helpers.parse_cameras_json(camera, max_limit = -1)
    return JsonResponse({'status': 200, 'message': 'Request Successfull!', 'totalResult': camera.count(), 'attributes': camera_json})
@csrf_exempt
@auth
def cameras_create(request):
    if request.method == 'GET':
        return Helpers.request_method_error('GET')
    request_body = json.loads(request.body.decode("utf-8"))
    camera = Camera(
        name=request_body['name'],
        address=request_body['address'],
        unique_id=request_body['unique_id'],
        lat=request_body['lat'],
        lon=request_body['lon']
    )
    camera.save()
    return JsonResponse({'status': 200, 'message': 'New Record Created!'})


@auth
def cameras_delete(request, id):
    if id is None:
        return JsonResponse({'status': 500, 'message': 'Id is required'})
    camera = Camera(id=id)
    camera.delete()
    return JsonResponse({'status': 200, 'message': 'Record Deleted!'})


@csrf_exempt
@auth
def cameras_update(request, id):
    if id is None:
        return JsonResponse({'status': 500, 'message': 'Id is required'})
    request_body = json.loads(request.body.decode("utf-8"))
    camera = Camera.objects.get(id=id)

    camera.name = request_body['name']
    camera.address = request_body['address']
    camera.unique_id = request_body['unique_id']
    camera.lat = request_body['lat']
    camera.lon = request_body['lon']

    camera.save()

    return JsonResponse({'status': 200, 'message': 'Record Updated'})


@csrf_exempt
def image_upload(request):
    if request.method == 'GET':
        return Helpers.request_method_error('GET')
    camera_id = request.POST['camera_id']
    created_at =  request.POST['created_at']
    camera = Camera.objects.filter(unique_id=camera_id)
    if (camera.count() >= 1):
        id = camera.first().id
        files = request.FILES
        for name in files:
            file = files[name];
            handle_uploaded_file(file, name);

            image = Image(
                name = name,
                camera_id = id,
                created_at = created_at
            )
            image.save()
            break;



    else:
        print('camers not exists')

    return JsonResponse({'status': 200, 'message': 'Record Updated'})


def handle_uploaded_file(file, name):
    with open(MEDIA_ROOT + name, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
