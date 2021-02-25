from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('motherboards/', views.motherboards, name='motherboards'),
    path('cpus/', views.cpus, name='cpus'),
    path('gpus/', views.gpus, name='gpus'),
    path('rammemories/', views.ram_memories, name='ram_memories'),
    path('storages/', views.storages, name='storages'),
    path('motherboards/<int:motherboard_id>', views.motherboard_detail, name='motherboard_detail'),
    path('cpus/<int:cpu_id>', views.cpu_detail, name='cpu_detail'),
    path('gpus/<int:gpu_id>', views.gpu_detail, name='gpu_detail'),
    path('storages/<int:storage_id>', views.storage_detail, name='storage_detail'),
    path('rammemories/<int:ram_id>', views.ram_memory_detail, name='ram_memory_detail'),
    path('buildpc/', views.computer_build, name='computer_build'),
    path('computers/', views.computers, name='computers'),
    path('computers/<int:computer_id>', views.computer_detail, name='computer_detail'),
]
