from django.db import models
from item.models import Item
from django.contrib.auth.models import User

# Create your models here.


class Conversation(models.Model):

    class Meta:
        ordering = ['-modifiedAt',]


    item = models.ForeignKey(Item, related_name='conversations', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversations')
    createdAt = models.DateTimeField(auto_now=True)
    modifiedAt = models.DateTimeField(auto_now=True)


class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)