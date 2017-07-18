from django.db import models
import django.utils 
import datetime
# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # add string method to give you some info when interacting w object
    def __str__(self):
        return self.question_text
    # can add any old method here 

    def is_recent(self):
        return self.pub_date >= django.utils.timezone.now() - datetime.timedelta(1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text