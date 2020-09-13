from django.contrib import admin
from .models import Post, Comment, Label, Author

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Label)
admin.site.register(Author)
