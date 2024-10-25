from django.contrib import admin
from .models import Post
from .models import Employer
from .models import User
admin.site.register(Post)
admin.site.register(Employer)
admin.site.register(User)


