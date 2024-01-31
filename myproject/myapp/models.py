from django.db import models

# create model

#Person = Table in DB
class Person(models.Model):
    #name age date = Field in DB
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name + ","+str(self.age)