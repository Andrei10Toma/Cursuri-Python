from django.shortcuts import render
from .models import *
from .forms import ComputerForm
from django.http import HttpResponseRedirect


def computer_build(response):
    storage_quantity = {}
    ram_quantity = {}
    built_pc = None
    form = ComputerForm(response.POST or None)
    data = dict(response.POST)
    context = {
        'form': form
    }
    if form.is_valid():
        if response.POST.get('next'):
            for computer in Computer.objects.all():
                if computer.name == data.get('name')[0]:
                    built_pc = computer
                    break
            if built_pc is None:
                built_pc = Computer(name=data.get('name')[0],
                                    motherboard=Motherboard.objects.get(id=response.POST.get('motherboard')),
                                    cpu=CPU.objects.get(id=response.POST.get('cpu')),
                                    gpu=GPU.objects.get(id=response.POST.get('gpu')),)
                built_pc.save()
                built_pc.ram_memory.add(*data.get('ram_memory'))
                built_pc.storage.add(*data.get('storage'))
            context['built_pc'] = built_pc
            if len(data) > 8:
                for ram_memory in built_pc.ram_memory.all():
                    if ram_memory.name in data.keys():
                        ram_quantity[int(ram_memory.id)] = int(data.get(ram_memory.name)[0])
                    else:
                        ram_quantity[ram_memory.id] = 0
                for storage in built_pc.storage.all():
                    if storage.name in data.keys():
                        storage_quantity[int(storage.id)] = int(data.get(storage.name)[0])
                    else:
                        storage_quantity[storage.id] = 0
                context['form'] = ComputerForm()
                context['built_pc'] = None
                built_pc.ram_quantity = ram_quantity
                built_pc.storage_quantity = storage_quantity
                built_pc.save()
                has_compatible_components, problems = built_pc.has_compatible_components()
                if has_compatible_components:
                    return HttpResponseRedirect('/buildyourpc/computers/')
                else:
                    built_pc.delete()
                    context['problems'] = problems
                    return render(response, 'buildyourpc/not_compatible.html', context=context)
    return render(response, 'buildyourpc/computer_build.html', context=context)


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


def computers(response):
    all_computers = Computer.objects.all()
    all_total_prices = {}
    for computer in all_computers:
        all_total_prices[computer.id] = computer.total_price
    context = {
        'all_computers': all_computers,
        'all_total_prices': all_total_prices,
    }
    return render(response, 'buildyourpc/computer_list.html', context=context)


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


def computer_detail(response, computer_id):
    name = Computer.objects.get(id=computer_id).name
    motherboard = Computer.objects.get(id=computer_id).motherboard
    cpu = Computer.objects.get(id=computer_id).cpu
    gpu = Computer.objects.get(id=computer_id).gpu
    all_ram_memory = Computer.objects.get(id=computer_id).ram_memory.all()
    all_storage = Computer.objects.get(id=computer_id).storage.all()
    ram_quantity = Computer.objects.get(id=computer_id).ram_quantity
    storage_quantity = Computer.objects.get(id=computer_id).storage_quantity
    total_price = str(Computer.objects.get(id=computer_id).total_price())
    context = {
        'name': name,
        'motherboard': motherboard,
        'cpu': cpu,
        'gpu': gpu,
        'all_ram_memory': all_ram_memory,
        'all_storage': all_storage,
        'ram_quantity': ram_quantity,
        'storage_quantity': storage_quantity,
        'total_price': total_price,
    }
    return render(response, 'buildyourpc/computer_detail.html', context=context)
