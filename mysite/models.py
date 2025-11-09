from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    comleted = models.BooleanField(default=False)
    
    def __str__(self): # this is a string representation of the model
        return self.title # return the title of the task