from django.db import models

class School(models.Model):
    name = models.CharField(max_length=255)      
    address = models.CharField(max_length=500)  

    def __str__(self):
        return self.name
class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    grade = models.CharField(max_length=50)
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="students"
    )
    def __str__(self):
        return f"{self.name} ({self.grade})"
class Teacher(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=100)

    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="teachers"
    )
    def __str__(self):
        return f"{self.name} - {self.subject}"
