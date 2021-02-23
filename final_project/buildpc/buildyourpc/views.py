from django.shortcuts import render
from .models import *


def home(response):
    context = {
        'num_motherboards': Motherboard.objects.all().count(),
        'num_cpus': CPU.objects.all().count(),
        'num_gpus': GPU.objects.all().count(),
        'num_storages': Storage.objects.all().count(),
        'num_ram_memory': MemoryRAM.objects.all().count(),
    }
    return render(response, 'buildyourpc/home.html', context=context)


def motherboards(response):
    all_motherboards = Motherboard.objects.all()
    context = {
        'all_motherboards': all_motherboards
    }
    return render(response, 'buildyourpc/motherboard_list.html', context=context)


def cpus(response):
    all_cpus = CPU.objects.all()
    context = {
        'all_cpus': all_cpus
    }
    return render(response, 'buildyourpc/cpu_list.html', context=context)


def gpus(response):
    all_gpus = GPU.objects.all()
    context = {
        'all_gpus': all_gpus
    }
    return render(response, 'buildyourpc/gpu_list.html', context=context)


def ram_memories(response):
    all_ram_memories = MemoryRAM.objects.all()
    context = {
        'all_ram_memories': all_ram_memories
    }
    return render(response, 'buildyourpc/ram_memory_list.html', context=context)


def storages(response):
    all_storages = Storage.objects.all()
    context = {
        'all_storages': all_storages
    }
    return render(response, 'buildyourpc/storage_list.html', context=context)


def motherboard_detail(response, motherboard_id):
    motherboard = Motherboard.objects.get(id=motherboard_id)
    context = {
        'name': motherboard.name,
        'cpu_socket': motherboard.cpu_socket,
        'memory_type': motherboard.memory_type,
        'max_memory': motherboard.max_memory,
        'memory_slots': motherboard.memory_slots,
        'sata_slots': motherboard.sata_slots,
        'price': motherboard.price,
    }
    return render(response, 'buildyourpc/motherboard_detail.html', context=context)


def cpu_detail(response, cpu_id):
    cpu = CPU.objects.get(id=cpu_id)
    context = {
        'name': cpu.name,
        'socket': cpu.socket,
        'manufacturer': cpu.get_manufacturer_display(),
        'frequency': cpu.frequency,
        'cores': cpu.cores,
        'price': cpu.price,
    }
    return render(response, 'buildyourpc/cpu_detail.html', context=context)


def gpu_detail(response, gpu_id):
    gpu = GPU.objects.get(id=gpu_id)
    context = {
        'name': gpu.name,
        'gpu_memory': gpu.gpu_memory,
        'price': gpu.price,
    }
    return render(response, 'buildyourpc/gpu_detail.html', context=context)


def storage_detail(response, storage_id):
    storage = Storage.objects.get(id=storage_id)
    context = {
        'name': storage.name,
        'type': storage.get_type_display(),
        'capacity': storage.capacity,
        'interface': storage.interface,
        'price': storage.price,
    }
    return render(response, 'buildyourpc/storage_detail.html', context=context)


def ram_memory_detail(response, ram_id):
    ram_memory = MemoryRAM.objects.get(id=ram_id)
    context = {
        'name': ram_memory.name,
        'memory_type': ram_memory.memory_type,
        'capacity': ram_memory.capacity,
        'frequency': ram_memory.frequency,
        'price': ram_memory.price,
    }
    return render(response, 'buildyourpc/ram_memory_detail.html', context=context)
