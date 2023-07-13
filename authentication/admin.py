from django.contrib import admin

# Register your models here.

from authentication.models.signup import signupUser

# Register your models here.
class NewUserAdmin(admin.ModelAdmin):
    list_display = ["__str__", "firstName", "lastName", "userName", "status", "email", "mobile", "register_on"]
    prepopulated_fields = {"slug": ("firstName", "lastName")}
    class Meta:
        model=signupUser
admin.site.register(signupUser, NewUserAdmin)

