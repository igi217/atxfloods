from django.urls import path

from . import views

urlpatterns = [
    path('auth/login', views.login, name='login'),
    path('counts', views.count, name='count'),
    path('', views.index, name='index'),
    path('auth/change-password', views.change_password, name='change_password'),
    path('crossings/all', views.all_crossings, name="all_crossings"),
    path('crossings/create', views.create_crossing, name='create_crossing'),
    path('crossings/import', views.import_crossing, name='import_crossing'),
    path('crossings/delete/<int:id>', views.delete_crossing, name='delete_crossing'),
    path('crossings/update/<int:id>', views.update_crossing, name='update_crossing'),
    path('closures', views.closures, name='closures'),
    path('cameras/all', views.cameras, name='cameras'),
    path('cameras/<int:id>', views.camera_single, name='camera_one'),
    path('cameras/create', views.cameras_create, name='cameras_create'),
    path('cameras/update/<int:id>', views.cameras_update, name='cameras_update'),
    path('cameras/delete/<int:id>', views.cameras_delete, name='cameras_delete'),
    path('cameras/upload', views.image_upload, name='camera.image_upload')
]