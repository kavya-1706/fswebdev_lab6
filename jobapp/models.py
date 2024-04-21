from django.db import models

# Create your models here.
class jobs_data(models.Model):
    job_Id = models.AutoField(primary_key=True)
    job_Name = models.CharField(max_length=100, blank=False, null=False )
    job_Company = models.CharField(max_length=100, blank=False, null=False)
    job_Location = models.CharField(max_length=100, blank=False, null=False)
    job_Description = models.CharField(max_length=100, blank=False, null=False)
    


    class Meta:
        db_table = 'jobs' 