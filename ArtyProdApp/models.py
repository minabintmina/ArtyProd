from django.db import models

class SignUp(models.Model):
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    username = models.CharField(max_length=100, unique=True, default='')
    email = models.EmailField(max_length=100, unique=True, default='')
    password = models.CharField(max_length=100, default='')
    
class Contact(models.Model):  
    subject=models.CharField(max_length=200, default='')
    text=models.CharField(max_length=1000, default='')
    sender_username = models.CharField(max_length=150, blank=True)
    
class Services(models.Model):
    CHOICES=(("Graphic charts","Graphic charts"),
        ("3D Modeling","3D Modeling"),
        ("Scriptwriting","Scriptwriting"))
    TypeS=models.CharField(max_length=20, choices=CHOICES)
    description=models.TextField()
    Photo=models.FileField(upload_to='services/')
    def __str__(self):
        return self.TypeS
    
class Personnel(models.Model):
    name=models.CharField(max_length=50)
    CV_File=models.FileField(upload_to='pdfs/')
    service = models.ManyToManyField(Services)
    experience = models.PositiveIntegerField(default=1)
    Photo_File=models.FileField(upload_to='photos/')
    linkedln_link=models.URLField(max_length=200)
 
class Team(models.Model):
    personnel = models.ManyToManyField(Personnel)
    def __str__(self):
        return ", ".join([personnel.name for personnel in self.personnel.all()])
       
class Project(models.Model):
    label=models.CharField(max_length=50, default='')
    service = models.ManyToManyField(Services)
    description=models.TextField(max_length=500, default='')
    start_date=models.DateField(null=True)
    end_date=models.DateField()
    CHOICE=(("C","Completed"),
            ("I","In-progress"),
            )
    status=models.CharField(max_length=1, choices=CHOICE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    sender_username = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.label
    
# Create your models here.
