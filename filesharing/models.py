from django.db import models


class FileEntity(models.Model):
    # we'll use id as an artificial file name on our server
    id = models.AutoField(primary_key=True)

    # file will get renamed a moment before downloading ideally
    filename = models.TextField(max_length=20)

    date_upload = models.DateTimeField(auto_now_add=True)
