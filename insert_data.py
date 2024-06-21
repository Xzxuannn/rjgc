import csv
from django.core.management.base import BaseCommand
from underwater.models import Fish
from underwater.models import WaterQuality
from underwater.models import Sensor
from datetime import datetime

'''
class Command(BaseCommand):
    help = 'Inserts fish data from CSV file into the database'

    
    def handle(self, *args, **kwargs):
        with open('underwater/data/fish.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Fish.objects.create(
                    species=row['Species'],
                    weight=float(row['Weight(g)']),
                    length1=float(row['Length1(cm)']),
                    length2=float(row['Length2(cm)']),
                    length3=float(row['Length3(cm)']),
                    height=float(row['Height(cm)']),
                    width=float(row['Width(cm)']),
                )
        self.stdout.write(self.style.SUCCESS('Data inserted successfully!'))
    
    
'''




def safe_date(date_str, default=None):
    formats_to_try = ['%Y-%m-%d %H:%M', '%Y-%m-%d', '%Y-%m-%d %H:%M:%S']
    for fmt in formats_to_try:
        try:
            return datetime.strptime(date_str, fmt)
        except (ValueError, TypeError):
            continue
    return default

class Command(BaseCommand):
    help = 'Inserts sensor data from a CSV file into the database'

    def handle(self, *args, **kwargs):
        file_path = 'underwater/data/sensor_data.csv'  # 修改为你的 CSV 文件路径

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                sensor_id = row['Sensor ID']
                sensor_type = row['Type']
                battery_level = int(row['Battery Level (%)'])
                next_maintenance_date = safe_date(row['Next Maintenance Date'])
                warranty_expiration_date = safe_date(row['Warranty Expiration Date'])
                start_date = safe_date(row['Start Date'])

                Sensor.objects.create(
                    sensor_id=sensor_id,
                    type=sensor_type,
                    battery_level=battery_level,
                    next_maintenance_date=next_maintenance_date,
                    warranty_expiration_date=warranty_expiration_date,
                    start_date=start_date
                )

        self.stdout.write(self.style.SUCCESS('Data inserted successfully!'))
