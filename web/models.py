from django.db import models
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="post/",blank=True,null=True)
    date_time = models.DateTimeField(auto_now_add=True)

    is_edited = models.BooleanField(default=False)
    class Meta:
        db_table = 'web_post'
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ('id',)
    
    def __str__(self):
        return self.title