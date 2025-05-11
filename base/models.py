from django.db import models

class Room(models.Model):
    # host = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    # topic = models.ForeignKey('Topic', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True) # take a snapshot and changes every single timeq
    created = models.DateTimeField(auto_now_add=True) # take a snapshot and changes only when the object is created

    def __str__(self):
        return self.name
