from django.db import models

# Create your models here.
class ObjectiveType(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return '%s' % self.name

# Create your models here.
class Objective(models.Model):
    name = models.CharField(max_length=64)
    type_id = models.ForeignKey(ObjectiveType,on_delete=models.SET_NULL,null=True,related_name='scenario_ids',db_column="type_id")
    description = models.ImageField(blank=True, null=True)

    def __str__(self):
        return '%s' % self.name

    def get_description_url(self):
        if self.description:
            return self.description.url
        else:
            return ''
