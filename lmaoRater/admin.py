from django.contrib import admin

# Register your models here.
from .models import WhiteCard, BlackCard, score

admin.site.register(WhiteCard)
admin.site.register(BlackCard)
admin.site.register(score)