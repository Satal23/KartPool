from django.db import migrations
import json
from django.contrib.gis.geos import fromstr
from pathlib import Path
from django.utils import timezone

DATA_FILENAME = 'data/data.json'
CITY = 'Irvine'

def load_data(apps, schema_editor):
    Store = apps.get_model('stores', 'Store')
    jsonfile = Path(__file__).parents[2] / DATA_FILENAME

    with open(str(jsonfile)) as datafile:
        objects = json.load(datafile)

        if 'elements' not in objects:
            raise ValueError("Expected 'elements' key not found in the JSON file.")

        for obj in objects['elements']:
            try:
                objType = obj['type']
                if objType == 'node':
                    tags = obj['tags']
                    name = tags.get('name', 'N/A')

                    lon = obj.get('lon', 0)
                    lat = obj.get('lat', 0)
                    location = fromstr(f'POINT({lon} {lat})', srid=4326)

                    housenumber = tags.get('addr:housenumber', 'N/A')
                    street = tags.get('addr:street', 'N/A')
                    postcode = tags.get('addr:postcode', 'N/A')
                    address = f"{housenumber}, {street}, {postcode}"

                    store_type = tags.get('shop', 'N/A')
                    phone = tags.get('phone', 'N/A')
                    
                    # Create the Store object
                    Store.objects.create(
                        id=obj['id'],  # Keep or modify this if needed
                        name=name,
                        lat=lat,
                        lon=lon,
                        location=location,
                        store_type=store_type,
                        phone=phone[:100],
                        address=address[:100],
                        city=CITY,
                        created_at=timezone.now()  # Set created_at to now
                    )
                    print(f"Added store: {name} at {lon}, {lat}")
                    
            except KeyError as e:
                print(f"KeyError: {e} for object: {obj}")
            except Exception as e:
                print(f"Error processing object: {obj}. Exception: {e}")

class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_store'),
    ]

    operations = [
        migrations.RunPython(load_data),
    ]
