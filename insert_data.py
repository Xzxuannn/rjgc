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


'''
def safe_float(value, default=None):
    try:
        return float(value)
    except ValueError:
        return default

class Command(BaseCommand):
    help = 'Inserts water quality data from multiple CSV files into the database'

    def insert_data_from_csv(self, file_path):
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # 解析监测时间
                try:
                    # 获取当前年份
                    current_year = datetime.now().year
                    # 解析月份和日期部分
                    monitoring_time = datetime.strptime(row['监测时间'], '%m-%d %H:%M')
                    # 将解析后的日期时间对象加上当前年份
                    monitoring_time = monitoring_time.replace(year=current_year)
                except ValueError:
                    # 跳过无效的监测时间
                    continue
                
                WaterQuality.objects.create(
                    section_name=row['断面名称'],
                    monitoring_time=monitoring_time,
                    water_quality_category=row['水质类别'],
                    water_temperature=safe_float(row['水温(℃)']),
                    pH=safe_float(row['pH(无量纲)']),
                    dissolved_oxygen=safe_float(row['溶解氧(mg/L)']),
                    conductivity=safe_float(row['电导率(μS/cm)']),
                    turbidity=safe_float(row['浊度(NTU)']),
                    permanganate_index=safe_float(row['高锰酸盐指数(mg/L)']),
                    ammonia_nitrogen=safe_float(row['氨氮(mg/L)']),
                    total_phosphorus=safe_float(row['总磷(mg/L)']),
                    total_nitrogen=safe_float(row['总氮(mg/L)']),
                    site_status=row['站点情况'],
                )
    def handle(self, *args, **kwargs):
        #csv_files = ['北洋桥.csv', '大红桥.csv', '大套桥.csv','海河大闸.csv','万家码头.csv']
        csv_files = ['add.csv']
        for file in csv_files:
            self.insert_data_from_csv(f'underwater/data/{file}')
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