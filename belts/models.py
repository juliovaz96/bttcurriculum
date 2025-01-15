from django.db import models

class Belt(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Technique(models.Model):
    belt = models.ForeignKey(Belt, on_delete=models.CASCADE, related_name='techniques')
    name = models.CharField(max_length=100)
    description = models.TextField()
    video_link = models.URLField(blank=True, null=True)  # Add this field

    # Optional: If you want to group by "Day", e.g., Day 1, Day 2, ...
    # day = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.belt.name})"
