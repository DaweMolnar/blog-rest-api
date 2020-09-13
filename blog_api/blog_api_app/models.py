from django.db import models


class Label(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return str(self.name)


class Author(models.Model):
    name = models.CharField(max_length=30, unique=True)
    profile_img_url = models.URLField()
    registration_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return str(self.name)


class Post(models.Model):
    author = models.ForeignKey(Author, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=120, unique=True)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    up_votes = models.PositiveIntegerField(default=0)
    down_votes = models.PositiveIntegerField(default=0)
    labels = models.ManyToManyField(Label, related_name='posts')

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    author = models.CharField(max_length=30)
    body = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    up_votes = models.PositiveIntegerField(default=0)
    down_votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.author)


