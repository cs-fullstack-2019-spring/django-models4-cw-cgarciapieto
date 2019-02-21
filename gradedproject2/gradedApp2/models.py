from django.db import models


#  models are created here.
class Mother(models.Model):
    mother_first_name = models.CharField(max_length=100)
    mother_last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.mother_first_name} {self.mother_last_name}'


class Child(models.Model):
    child_first_name = models.CharField(max_length=100)
    child_last_name = models.CharField(max_length=100)
    child_mom = models.ForeignKey(Mother, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.child_first_name}'
