from django.contrib import admin
from userstuff.models import User, Song, UserProfile

# blog postlarımızın admin kısmından erişilebilir olmasını sağlıyor.
admin.site.register(User)
admin.site.register(UserProfile)
# admin.site.register(UserFollowing)
admin.site.register(Song)
