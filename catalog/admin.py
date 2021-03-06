from django.contrib import admin

# Register your models here.

from catalog.models import Author, Genre, Book, BookInstance, Language

#Define the admin class
class BookAdminInline(admin.TabularInline):
    model = Book
    extra = 0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookAdminInline]

#Register the admin class with the associated model

# Register the Admin classes for Book using the decorator

class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]


# Register the Admin classes for BookInstance using the decorator

class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'imprint', 'status')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

admin.site.register(BookInstance, BookInstanceAdmin)

admin.site.register(Language)
admin.site.register(Genre)
