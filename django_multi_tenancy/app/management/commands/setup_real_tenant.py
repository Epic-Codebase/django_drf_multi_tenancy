from django.core.management.base import BaseCommand
from app.models import Tenant, Domain

class Command(BaseCommand):
    help = 'Run initial setup for model persistence'

    def handle(self, *args, **kwargs):
      
        # create your first real tenant
        tenant = Tenant(schema_name='tenant1',
                        name='Fonzy Tenant',
                        paid_until='2014-12-05',
                        on_trial=True)
        tenant.save() # migrate_schemas automatically called, your tenant is ready to be used!

        # Add one or more domains for the tenant
        domain = Domain()
        domain.domain = 'tenant.localhost' # don't add your port or www here! (We are not using domain-based tenants in this sample)
        domain.tenant = tenant
        domain.is_primary = True
        domain.save()