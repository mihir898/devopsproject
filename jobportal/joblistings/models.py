from django.db import models

# Create your models here.

class JobPost(models.Model):
    job_title = models.CharField(max_length=200)
    experience_level = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    job_description = models.CharField(max_length=5000)
    job_type = models.CharField(max_length=100)

    def __str__(self):
        return self.job_title+": "+self.company_name

class JobApplication(models.Model):
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_no = models.CharField(max_length=200)
    skills = models.CharField(max_length=1000)
    experience = models.IntegerField()

    def __str__(self):
        return self.full_name
