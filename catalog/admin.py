from django.contrib import admin

# Register your models here.

from catalog.models import Author, Genre, Book, BookInstance, Language

#Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    pass

#Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# Register the Admin classes for Book using the decorator
admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

# Register the Admin classes for BookInstance using the decorator
admin.site.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin)
    pass


admin.site.register(Language)
admin.site.register(Genre)
