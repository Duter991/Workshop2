from django.contrib import admin
from authentification.models import Token

# Register your models here.

class TokenFinder(admin.ModelAdmin):
    list_display= ('user', 'token')

admin.site.register(Token, TokenFinder)
