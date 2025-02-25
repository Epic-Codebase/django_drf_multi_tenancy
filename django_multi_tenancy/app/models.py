from django.db import models
from django_tenants.models import DomainMixin, TenantMixin

class Tenant(TenantMixin): # A registered client
    name = models.CharField(max_length=100, unique=True)
    paid_until = models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)
    auto_create_schema = True


class Domain(DomainMixin):
    pass
