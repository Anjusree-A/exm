from django.db.models.signals import  pre_save
from django.dispatch import receiver
from django.template.defaultfilters import upper

from myapp.models import Employee
@receiver(pre_save, sender=Employee)
def uppercase_username(sender,instance,**kwargs):
    instance.name=instance.name.upper()

