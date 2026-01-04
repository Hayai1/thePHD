from django.db import models



class Tour(models.Model):
    date = models.DateField()
    venue = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    ticket_link = models.URLField(blank=True, null=True)  # link for tickets

    def __str__(self):
        return f"{self.date} - {self.venue}"
