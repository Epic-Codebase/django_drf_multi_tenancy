from django.core.management.base import BaseCommand
from app.models import Tenant, Domain

class Command(BaseCommand):
    help = 'Run initial setup for model persistence'

    def handle(self, *args, **kwargs):
       
        # create your public tenant
        tenant = Tenant(schema_name='public',
                        name='Schemas Inc.',
                        paid_until='2016-12-05',
                        on_trial=False)
        tenant.save()

        # Add one or more domains for the tenant
        domain = Domain()
        domain.domain = 'localhost' # don't add your port or www here! on a local server you'll want to use localhost here
        domain.tenant = tenant
        domain.is_primary = True
        domain.save()