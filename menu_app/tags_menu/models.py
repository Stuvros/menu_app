from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    menu_name = models.CharField(max_length=50)
    order = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.menu_name} ({self.name})"