from django.contrib import admin

from .models import Profile, Categories, Add_a_recipe_Model, CommentModel

admin.site.register(Profile)
admin.site.register(Categories)
admin.site.register(Add_a_recipe_Model)
admin.site.register(CommentModel)


