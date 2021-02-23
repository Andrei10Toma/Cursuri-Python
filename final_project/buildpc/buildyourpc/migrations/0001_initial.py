# Generated by Django 3.1.6 on 2021-02-22 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the CPU', max_length=200)),
                ('socket', models.CharField(help_text='Socket of the CPU (e.g. AM4)', max_length=200)),
                ('manufacturer', models.CharField(blank=True, choices=[('a', 'AMD'), ('i', 'Intel')], default='i', help_text='Manufacturer of the CPU', max_length=1)),
                ('frequency', models.IntegerField()),
                ('cores', models.IntegerField()),
                ('price', models.FloatField()),
            ],
            options={
                'ordering': ['manufacturer'],
            },
        ),
        migrations.CreateModel(
            name='GPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the GPU', max_length=200)),
                ('gpu_memory', models.IntegerField()),
                ('price', models.FloatField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MemoryRAM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the memory.', max_length=200)),
                ('memory_type', models.CharField(help_text='Memory type (e.g DDR4, DDR3)', max_length=200)),
                ('capacity', models.IntegerField()),
                ('frequency', models.IntegerField()),
                ('price', models.FloatField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Motherboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the motherboard', max_length=200)),
                ('cpu_socket', models.CharField(help_text='Compatible CPU socket', max_length=200)),
                ('memory_type', models.CharField(help_text='Type of the memory(e.g. DDR3, DDR4)', max_length=200)),
                ('max_memory', models.IntegerField()),
                ('memory_slots', models.IntegerField()),
                ('sata_slots', models.IntegerField()),
                ('price', models.FloatField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the storage.', max_length=200)),
                ('type', models.CharField(blank=True, choices=[('h', 'HDD'), ('s', 'SSD')], default='h', help_text='Storage type', max_length=1)),
                ('capacity', models.IntegerField()),
                ('interface', models.CharField(help_text='Interface of the storage memory(e.g. SATA III)', max_length=200)),
                ('price', models.FloatField()),
            ],
            options={
                'ordering': ['type'],
            },
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the computer.', max_length=200)),
                ('cpu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buildyourpc.cpu')),
                ('gpu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buildyourpc.gpu')),
                ('motherboard', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buildyourpc.motherboard')),
                ('ram_memory', models.ManyToManyField(to='buildyourpc.MemoryRAM')),
                ('storage', models.ManyToManyField(to='buildyourpc.Storage')),
            ],
        ),
    ]
