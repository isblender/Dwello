from django.db import models
from users.models import User
from apartments.models import Apartment

class Conversation(models.Model):
    initiator = models.ForeignKey(User, related_name='initiated_conversations', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_conversations', on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
