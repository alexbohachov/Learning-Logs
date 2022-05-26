from django.db import models


class Topic(models.Model):
    """ The topic the user is studying  """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Returns a string representation of the model  """
        return self.text

class Entry(models.Model):
    """Information explored by the user on a topic """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """ Returns a string representation of the model  """
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return f"{self.text[:50]}"