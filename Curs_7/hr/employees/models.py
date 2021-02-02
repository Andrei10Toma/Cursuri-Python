from django.db import models


class MyModel(models.Model):
    class Meta:
        abstract = True
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Employer(MyModel):
    class Meta:
        db_table = "employees_employer"
    name = models.CharField(max_length=255, unique=True)
