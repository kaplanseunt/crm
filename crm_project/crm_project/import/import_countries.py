# import_countries.py
import os
import sys

# Django projesinin ana dizinini ekleyin
sys.path.append('/Users/tahakaplan/tk/CRM4/crm_project/')

# Django ayarlarını yükleyin
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crm_project.settings")
import django
django.setup()

import json
from crmapp.models import Country

def import_countries():
    with open('/Users/tahakaplan/tk/CRM4/crm_project/countries.json', 'r') as file:
        countries_data = json.load(file)

    for country_data in countries_data['countries']:
        Country.objects.create(
            sortname=country_data['sortname'],
            name=country_data['name'],
            phonecode=country_data['phoneCode']
        )

if __name__ == '__main__':
    import_countries()
