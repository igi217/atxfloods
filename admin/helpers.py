from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.core.files.storage import FileSystemStorage
from .models import Crossing, Image
import pandas
import json
import base64


class Helpers:
    def parse_crossings_json(page_obj):
        statuses = {1: 'open', 0: 'closed', 2: 'caution'}
        data = []
        for crossing in page_obj:
            crossing_dict = {
                'id': crossing.id,
                'name': crossing.name,
                'jurisdiction': crossing.jurisdiction,
                'address': crossing.address,
                'lat': crossing.lat,
                'lon': crossing.lon,
                'comment': crossing.comment,
                'status': statuses[crossing.status],
                'created_at': crossing.created_at,
                'updated_at': crossing.updated_at

            }

            data.append(crossing_dict)

        return data

    def parse_cameras_json(page_obj):
        data = []
        for camera in page_obj:
            camera_dict = {
                'id': camera.id,
                'unique_id': camera.unique_id,
                'name' : camera.name,
                'address': camera.address,
                'lat': camera.lat,
                'lon': camera.lon,
                'updated_at': camera.updated_at,
                'images': parse_camera_images(camera.id)
            }
            data.append(camera_dict)
        return data
    def request_method_error(method):
        return JsonResponse({'status': 500, 'message': method + " method is not Allowed!"})


def auth(f):
    def wrap(request, *args, **kwargs):
        if 'Authorization' not in request.headers:
            return JsonResponse({'status': 403, 'message': 'Unauthenticated Request'})

        _token = request.headers['Authorization']
        token_bytes = _token.encode('ascii')
        base64_bytes = base64.b64decode(token_bytes)
        token = base64_bytes.decode('ascii')
        credentials = json.loads(token)
        user = authenticate(username=credentials['username'],
                            password=credentials['password'])
        # this check the session if userid key exist, if not it will redirect to login page
        if user is None:
            return JsonResponse({'status': 403, 'message': 'Unauthenticated Request'})
        request.user = user
        return f(request, *args, **kwargs)
    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap

def parse_camera_images(camera_id):
    images = Image.objects.filter(camera_id = camera_id).order_by('-id')
    data = []
    for index, image in enumerate(images):
        if index == 6 :
            break
        image_dict = {
            'image_name' : image.name,
            'created_at': image.created_at
        }

        data.append(image_dict)
    return data
def handle_csv_import(file):
    errors = []
    warnings = []
    success = 0
    statusDict = {
        'on' : 1,
        'off' : 0,
        'caution' : 2
    }
    fs = FileSystemStorage()
    filename = fs.save(file.name, file)
    path = fs.path(filename)
    data = pandas.read_excel(path)

    data_dict = data.to_dict('records')
    for index, record in enumerate(data_dict):
        if not record['Marker Name']:
            errors.append("Error at Row "+str(index+1)+" Marker Name is Required")
            continue
        elif not record['Address']:
            errors.append("Error at Row "+str(index+1)+" Address is Required")
            continue
        elif not record['Latitude']:
            errors.append("Error at Row "+str(index+1)+" Latitude is Required")
            continue
        elif not record['Longitude']:
            errors.append("Error at Row "+str(index+1)+" Longitude is Required")
            continue
        crossing_with_address = Crossing.objects.filter(
            address=record['Address'])
        if crossing_with_address.count() > 0:
            warnings.append("Skipping Row "+str(index+1) +
                            " Because it looks like duplicate of a available Record")
            continue

        crossing = Crossing(
            name=record['Marker Name'],
            jurisdiction=record['Jurisdiction'],
            address=record['Address'],
            lat=record['Latitude'],
            lon=record['Longitude'],
            comment=record['Comment'],
            status=statusDict[str(record['Type'])],
        )
        crossing.save()
        success+=1
        
    fs.delete(filename)

    return {'errors' : errors, 'warnings' : warnings, 'successfull': success}
