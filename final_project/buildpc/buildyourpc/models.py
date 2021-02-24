from django.db import models


class CPU(models.Model):
    name = models.CharField(
        max_length=200,
        help_text='Name of the CPU'
    )
    socket = models.CharField(
        max_length=200,
        help_text='Socket of the CPU (e.g. AM4)'
    )
    MANUFACTURER = (
        ('a', 'AMD'),
        ('i', 'Intel'),
    )
    manufacturer = models.CharField(
        max_length=1,
        choices=MANUFACTURER,
        blank=True,
        default='i',
        help_text='Manufacturer of the CPU'
    )
    frequency = models.FloatField()
    cores = models.IntegerField()
    price = models.FloatField()

    class Meta:
        ordering = ['manufacturer']

    def __str__(self):
        return f'{self.name} | {self.price} lei'


class Motherboard(models.Model):
    name = models.CharField(
        max_length=200,
        help_text='Name of the motherboard'
    )
    cpu_socket = models.CharField(
        max_length=200,
        help_text='Compatible CPU socket'
    )
    memory_type = models.CharField(
        max_length=200,
        help_text='Type of the memory(e.g. DDR3, DDR4)'
    )
    max_memory = models.IntegerField()
    memory_slots = models.IntegerField()
    sata_slots = models.IntegerField()
    price = models.FloatField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} | {self.price} lei'


class GPU(models.Model):
    name = models.CharField(
        max_length=200,
        help_text='Name of the GPU'
    )
    gpu_memory = models.IntegerField()
    price = models.FloatField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} | {self.price} lei'


class MemoryRAM(models.Model):
    name = models.CharField(
        max_length=200,
        help_text='Name of the memory.'
    )
    memory_type = models.CharField(
        max_length=200,
        help_text='Memory type (e.g DDR4, DDR3)'
    )
    capacity = models.IntegerField()
    frequency = models.FloatField()
    price = models.FloatField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} | {self.price} lei'


class Storage(models.Model):
    name = models.CharField(
        max_length=200,
        help_text='Name of the storage.'
    )
    STORAGE_TYPES = (
        ('h', 'HDD'),
        ('s', 'SSD')
    )
    type = models.CharField(
        max_length=1,
        choices=STORAGE_TYPES,
        blank=True,
        default='h',
        help_text='Storage type'
    )
    capacity = models.IntegerField()
    interface = models.CharField(
        max_length=200,
        help_text='Interface of the storage memory(e.g. SATA III)'
    )
    price = models.FloatField()

    class Meta:
        ordering = ['type']

    def __str__(self):
        return f'{self.name} | {self.price} lei'


class Computer(models.Model):
    name = models.CharField(
        max_length=200,
        help_text='Name of the computer.',
    )
    motherboard = models.ForeignKey(Motherboard, on_delete=models.CASCADE, null=True)
    cpu = models.ForeignKey(CPU, on_delete=models.CASCADE, null=True)
    gpu = models.ForeignKey(GPU, on_delete=models.CASCADE, null=True)
    ram_memory = models.ManyToManyField(MemoryRAM)
    storage = models.ManyToManyField(Storage)
    ram_quantity = {}
    storage_quantity = {}

    @property
    def has_compatible_components(self):
        if self.motherboard.cpu_socket != self.cpu.socket:
            return False
        return True

    @property
    def total_price(self):
        total_price_ram = 0
        total_price_storage = 0
        for ram_memory in self.ram_memory.all():
            if ram_memory.id in self.ram_quantity.keys():
                total_price_ram += ram_memory.price * float(self.ram_quantity.get(ram_memory.id)[0])
        for storage in self.storage.all():
            if storage.id in self.storage_quantity.keys():
                total_price_storage += storage.price * float(self.storage_quantity.get(storage.id)[0])
        return self.motherboard.price + self.cpu.price + self.gpu.price + total_price_storage + total_price_ram

    def __str__(self):
        return self.name
