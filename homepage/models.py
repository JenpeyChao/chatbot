from django.db import models
import uuid
# Create your models here.

class ChatInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    history = models.JSONField(default=list)# Stores chat messages
    # something like this ({
    #         'sender': question,
    #         'bot': answer,
    #         'timestamp': str(timezone.now()),
    #         'message_id': str(uuid.uuid4())
    #     })
    created_at = models.DateTimeField(auto_now_add=True)
    last_accessed = models.DateTimeField(auto_now=True)

    # No __init__ needed Django handles this
    # Just use ChatInstance.objects.create()
