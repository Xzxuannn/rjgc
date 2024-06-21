from django.db import models
from django.utils.timezone import now

# Create your models here.
class Fish(models.Model):
    species = models.CharField(max_length=50)
    weight = models.FloatField()
    length1 = models.FloatField()
    length2 = models.FloatField()
    length3 = models.FloatField()
    height = models.FloatField()
    width = models.FloatField()

    def __str__(self):
        return self.species
    

class WaterQuality(models.Model):
    
    ammonia_nitrogen = models.FloatField(null=True, blank=True)
    total_phosphorus = models.FloatField(null=True, blank=True)
    total_nitrogen = models.FloatField(null=True, blank=True)
    site_status = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.section_name} - {self.monitoring_time.strftime("%Y-%m-%d %H:%M")}'
    


class Sensor(models.Model):
    SENSOR_TYPES = [
        ('Turbidity', 'Turbidity'),
        ('Temperature', 'Temperature'),
        ('pH', 'pH'),
        ('Dissolved Oxygen', 'Dissolved Oxygen'),
        ('Conductivity', 'Conductivity'),
        ('Ammonia Nitrogen', 'Ammonia Nitrogen'),
        ('Nitrogen', 'Nitrogen'),
        ('Phosphorus', 'Phosphorus'),
        ('Permanganate', 'Permanganate'),
    ]

    sensor_id = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=20, choices=SENSOR_TYPES)
    battery_level = models.PositiveIntegerField()
    next_maintenance_date = models.DateTimeField()
    warranty_expiration_date = models.DateField()
    start_date = models.DateField()

    def get_running_time(self):
        current_date = now().date()  # 只获取当前时间的日期部分
        running_time = current_date - self.start_date
        print(f"Current date: {current_date}, Start date: {self.start_date}, Running time: {running_time.days}")
        return running_time.days