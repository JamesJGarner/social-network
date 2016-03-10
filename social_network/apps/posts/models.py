from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

	user = models.ForeignKey(
		User
		)

	text = models.TextField(
		null=True,
		)

	image = models.ImageField(
		upload_to='faces/',
		blank=True,
		null=True,
	)

	date = models.DateTimeField(
		null=True,
		)

	def __unicode__(self):
		return self.text

	class Meta:
		ordering = ['-date']

	@models.permalink
	def get_absolute_url(self):
			return ("posts:detail_post", (), {
				"pk": self.pk
			})


class Reply(models.Model):

	user = models.ForeignKey(
		User,
		related_name="user_replying"
		)

	post = models.ForeignKey(
		Post
		)

	text = models.CharField(
		null=True,
		max_length=100,
		)

	date = models.DateTimeField(
		null=True,
		)




