from django.db import models
from django.utils import timezone

# Create your models here.



CATEGORY_CHOICES = (
	('Select', 'Select'),
    ('Technical', 'Technical'),
    ('Non Technical', 'Non Technical'),
    ('Finance', 'Finance'),
    ('Sap', 'Sap'),
    ('Ca', 'Ca'),
    ('Business Development', 'Business Development'),
    ('others','others')
    )
JOB_CATEGORY_CHOICES = (
	('Select', 'Select'),
        ('Fulltime', 'Fulltime'),
        ('Contract', 'Contract'),
        ('hourly', 'hourly'),
    )
icon = (
	("fa fa-briefcase","fa fa-briefcase"),
        ('fa fa-user ', 'fa fa-user'),
        ('fa fa-book','fa fa-book'),
        ('fa fa-group', 'fa fa-group'),
        ('fa fa-building ', 'fa fa-building '),
    )



class Services(models.Model):
    service_name = models.CharField(max_length=100,verbose_name="Service Name")
    dics = models.CharField(max_length=200,verbose_name="Description")
    link = models.CharField(verbose_name="Service Page Url",max_length=100)
    icon = models.CharField(choices=icon,max_length=50,verbose_name="Icon")
    number = models.IntegerField()

    def __str__(self):
        return self.service_name

    class Meta:
        ordering = ["number"]

class Seminar_Webinar(models.Model):
    topic       =    models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    topic_name  =    models.CharField(max_length=100)
    content     =    models.TextField()
    long        =    models.BooleanField(default=0)
    lat         =    models.BooleanField(default=0)
    image       =    models.FileField()
    created_at  =    models.DateTimeField(auto_now_add=True) 
    updated_at  =    models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.topic



class Workshop(models.Model):
    topic           =       models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    topic_name      =       models.CharField(max_length=100)
    content         =       models.TextField()
    long            =       models.BooleanField(default=0)
    lat             =       models.BooleanField(default=0)
    image           =       models.FileField()
    created_at      =       models.DateTimeField(auto_now_add=True) 
    updated_at      =       models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.topic


class Training(models.Model):
    topic           =    models.CharField(max_length=20,choices=CATEGORY_CHOICES)
    topic_name      =    models.CharField(max_length=100)
    img             =    models.ImageField(upload_to="media")
    content         =    models.CharField(max_length=200)
    created_at      =    models.DateTimeField(auto_now_add=True) 
    updated_at      =    models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.topic






class Internship(models.Model):
    internship_categeory    =   models.CharField(max_length=30,choices=CATEGORY_CHOICES)
    title                   =   models.CharField(max_length=30)
    subject                 =   models.CharField(max_length=20)
    company                 =   models.CharField(max_length=30)
    work_type               =   models.CharField(max_length=30,choices=JOB_CATEGORY_CHOICES)
    created_at              =   models.DateTimeField(auto_now_add=True) 
    updated_at              =   models.DateTimeField(auto_now_add=True)  


    def __str__(self):
        return self.title



class Job(models.Model):
    job_categeory   =   models.CharField(max_length=30,choices=CATEGORY_CHOICES)
    jobtitle        =   models.CharField(max_length=30)
    location        =   models.CharField(max_length=20)
    vacancycount    =   models.IntegerField(blank=True)
    created_at      =   models.DateTimeField(auto_now_add=True) 
    updated_at      =   models.DateTimeField(auto_now_add=True)  


    def __str__(self):
        return self.jobtitle



class Industrial_Trainging(models.Model):
    training_categeory  =   models.CharField(max_length=20,choices=CATEGORY_CHOICES)
    image               =   models.ImageField()
    company             =   models.CharField(max_length=50)
    created_at          =   models.DateTimeField(auto_now_add=True) 
    updated_at          =   models.DateTimeField(auto_now_add=True)  


    def __str__(self):
        return self.training_categeory


class PortFollio(models.Model):
    filter = models.CharField(max_length=10,verbose_name="Category")
    title = models.CharField(max_length=10,verbose_name="Title")
    img = models.ImageField(upload_to="port/")
    link = models.URLField(blank=True)
    number = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-number"]



    


































