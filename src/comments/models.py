from django.db import models
from django.conf import settings

# Create your models here.
from posts.models import Post
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Comment(models.Model):
	user      = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.DO_NOTHING)
	#post      = models.ForeignKey(Post, on_delete=models.DO_NOTHING)

	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
	object_id = models.PositiveIntegerField(null=True)
	content_object = GenericForeignKey('content_type', 'object_id')

	content   = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
