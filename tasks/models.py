from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=255)
    start = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    complete = models.BooleanField()
    tags = models.ManyToManyField("Tag", related_name="tags")


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.name}"
