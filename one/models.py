from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class client(models.Model):
    cl_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    cl_phn_no = models.CharField(max_length=13, null=True)
    cl_name = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return self.cl_name
    


class salon(models.Model):
    TYPE=(
        ('Both', 'Both'),
        ('Ladies', 'Ladies'),
        ('Gentleman', 'Gentleman')
    )
    sal_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    sal_name = models.CharField(max_length=30, null=True)
    sal_phn_no = models.CharField(max_length=13, null=True)
    sal_adr = models.CharField(max_length=30, null=True)
    sal_otime = models.TimeField()
    sal_ctime = models.TimeField()
    sal_about = models.TextField(blank=True,null=True)
    type = models.CharField(max_length=15, choices=TYPE, null=True)
    
    def __str__(self):
        return self.sal_name

class services(models.Model):
    MIN=(
        (10,'10 Minutes'),
        (20,'20 Minutes'),
        (30,'30 Minutes'),
        (40,'40 Minutes'),
        (50,'50 Minutes'),
    )
    HOUR=(
        (0,0),
        (1,'1 Hour'),
        (2,'2 Hour'),
        (3,'3 Hour'),
        (4,'4 Hour'),
        (5,'5 Hour'),
        (6,'6 Hour'),
        (7,'7 Hour'),
    )
    s_name=models.CharField(max_length=20,null=True)
    s_price=models.FloatField(null=True)
    s_emin=models.IntegerField(null=True,choices=MIN)
    s_ehour=models.IntegerField(null=True,choices=HOUR)
    s_salon=models.ForeignKey(salon, on_delete=models.CASCADE,null=True)
    s_about=models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.s_name
    
class apointment(models.Model):
    MIN=(
        (10,'10 Minutes'),
        (20,'20 Minutes'),
        (30,'30 Minutes'),
        (40,'40 Minutes'),
        (50,'50 Minutes'),
    )
    HOUR=(
        (0,0),
        (1,'1 Hour'),
        (2,'2 Hour'),
        (3,'3 Hour'),
        (4,'4 Hour'),
        (5,'5 Hour'),
        (6,'6 Hour'),
        (7,'7 Hour'),
    )
    STATUS=(
        ('Pending','Pending'),
        ('Accept','Accept'),
        ('Done','Done'),
        ('Reject','Reject'),
        ('Absent','Absent'),
    )
    #on delete cascade?
    #one to one?
    a_salon=models.ForeignKey(salon, on_delete=models.CASCADE,null=True)
    a_client=models.ForeignKey(client, on_delete=models.CASCADE,null=True)
    a_status=models.CharField(choices=STATUS,default='Pending',max_length=20)
    a_service=models.ManyToManyField(services,related_name='apoint_service')
    a_total_price=models.FloatField(null=True)
    a_emin=models.IntegerField(null=True,choices=MIN)
    a_ehour=models.IntegerField(null=True,choices=HOUR)
    
    
    def __str__(self):
        return f"{self.a_salon.sal_user}|{self.a_client.cl_user}"


class cart(models.Model):
    c_salon=models.ForeignKey(salon, on_delete=models.CASCADE,null=True)
    c_client=models.ForeignKey(client, on_delete=models.CASCADE,null=True)
    c_service=models.ManyToManyField(services,related_name='cart_service')  
    
    def __str__(self):
        return f"{self.c_salon.sal_user}|{self.c_client.cl_user}"