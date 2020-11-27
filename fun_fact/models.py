from django.db import models


class FunFactSubmission(models.Model):
    username = models.CharField(max_length=50, blank=False)
    fun_fact = models.TextField(blank=False)

    def __str__(self):
        return "{} - {}".format(self.id, self.username)
