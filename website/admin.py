from django.contrib import admin
#from .models import Author, Genre, Book, BookInstance
from .models import Post, Newsletters


# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(Genre)
# admin.site.register(BookInstance)

# admin.site.register(Author)

# Define the admin class
# class PostAdmin(admin.ModelAdmin):
#     pass

# Register the admin class with the associated model
# admin.site.register(Post, PostAdmin)
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site
# admin.site.register(Book)
# admin.site.register(BookInstance)

# Register the Admin classes for Book using the decorator
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     pass

# # Register the Admin classes for BookInstance using the decorator
# @admin.register(PostInstance)
# class BookInstanceAdmin(admin.ModelAdmin):
#     pass

class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "ipaddress",'time','name', 'email', 'message')

admin.site.register(Post, PostAdmin)

#admin.site.register(Post)

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('time', 'ipaddress', 'email')

admin.site.register(Newsletters, NewsletterAdmin)

# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'display_genre')

# def display_genre(self):
#     """Create a string for the Genre. This is required to display genre in Admin."""
#     return ', '.join(genre.name for genre in self.genre.all()[:3])

# display_genre.short_description = 'Genre'

# class BookInstanceAdmin(admin.ModelAdmin):
#     list_filter = ('status', 'due_back')

# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

#     fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# @admin.register(BookInstance)
# class BookInstanceAdmin(admin.ModelAdmin):
#     list_filter = ('status', 'due_back')

#     fieldsets = (
#         (None, {
#             'fields': ('book', 'imprint', 'id')
#         }),
#         ('Availability', {
#             'fields': ('status', 'due_back')
#         }),
#     )

# class BooksInstanceInline(admin.TabularInline):
#     model = BookInstance

# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'display_genre')

#     inlines = [BooksInstanceInline]
