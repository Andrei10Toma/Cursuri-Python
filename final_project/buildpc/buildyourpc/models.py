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
    ram_quantity = models.JSONField(default=dict)
    storage_quantity = models.JSONField(default=dict)

    def has_compatible_components(self):
        problems = []
        is_compatible = True
        is_compatible = self.same_socket(is_compatible, problems)
        is_compatible = self.same_memory_type_motherboard(is_compatible, problems)
        is_compatible = self.check_ram_total_memory(is_compatible, problems)
        is_compatible = self.check_number_of_ram_memories(is_compatible, problems)
        is_compatible = self.check_storage_slots(is_compatible, problems)
        is_compatible = self.same_ram_memory_type_and_frequency(is_compatible, problems)
        return is_compatible, problems

    def same_ram_memory_type_and_frequency(self, is_compatible, problems):
        for ram_memory_1 in self.ram_memory.all():
            for ram_memory_2 in self.ram_memory.all():
                if ram_memory_1.memory_type != ram_memory_2.memory_type:
                    problems.append(f'RAM memory should be of the same type. {ram_memory_1.memory_type} '
                                    f'and {ram_memory_2.memory_type}')
                    is_compatible = False
                if ram_memory_1.frequency != ram_memory_2.frequency:
                    problems.append(f'RAM memory should have the same frequency. {ram_memory_1.frequency}'
                                    f' and {ram_memory_2.frequency}')
                    is_compatible = False
        return is_compatible

    def check_storage_slots(self, is_compatible, problems):
        if self.number_of_storage() > self.motherboard.sata_slots:
            is_compatible = False
            problems.append(f'Motherboard has {self.motherboard.sata_slots} slots for HDD or SSD and you selected'
                            f' {self.number_of_storage()} products.')
        return is_compatible

    def check_number_of_ram_memories(self, is_compatible, problems):
        if self.number_of_ram() > self.motherboard.memory_slots:
            problems.append(f'Motherboard has {self.motherboard.memory_slots} slots and you selected'
                            f' {self.number_of_ram()} products.')
            is_compatible = False
        return is_compatible

    def check_ram_total_memory(self, is_compatible, problems):
        if self.ram_total_memory() > self.motherboard.max_memory:
            problems.append(f'Motherboard has a maximum of {self.motherboard.max_memory} GB and the '
                            f'sum of all memory ram is {self.ram_total_memory()} GB')
            is_compatible = False
        return is_compatible

    def same_memory_type_motherboard(self, is_compatible, problems):
        for ram_memory in self.ram_memory.all():
            if ram_memory.memory_type != self.motherboard.memory_type:
                problems.append(f'Motherboard and RAM memory should have the same memory type RAM has '
                                f'{ram_memory.memory_type} and the motherboard has {self.motherboard.memory_type}')
                is_compatible = False
        return is_compatible

    def same_socket(self, is_compatible, problems):
        if self.motherboard.cpu_socket != self.cpu.socket:
            problems.append(f'Motherboard and CPU must have the same socket. The motherboard has '
                            f'{self.motherboard.cpu_socket} and the CPU {self.cpu.socket}')
            is_compatible = False
        return is_compatible

    def number_of_ram(self):
        total_quantity = 0
        for quantity in self.ram_quantity.values():
            total_quantity += int(quantity)
        return total_quantity

    def number_of_storage(self):
        total_storage = 0
        for quantity in self.storage_quantity.values():
            total_storage += int(quantity)
        return total_storage

    def ram_total_memory(self):
        total_memory_ram = 0
        for ram_memory in self.ram_memory.all():
            if ram_memory.id in self.ram_quantity.keys():
                total_memory_ram += ram_memory.capacity * float(self.ram_quantity.get(ram_memory.id))
        return total_memory_ram

    def total_price(self):
        total_price_ram = 0
        total_price_storage = 0
        for ram_memory in self.ram_memory.all():
            if str(ram_memory.id) in self.ram_quantity.keys():
                total_price_ram += ram_memory.price * float(self.ram_quantity.get(str(ram_memory.id)))
        for storage in self.storage.all():
            if str(storage.id) in self.storage_quantity.keys():
                total_price_storage += storage.price * float(self.storage_quantity.get(str(storage.id)))
        return self.motherboard.price + self.cpu.price + self.gpu.price + total_price_storage + total_price_ram

    def __str__(self):
        return self.name
