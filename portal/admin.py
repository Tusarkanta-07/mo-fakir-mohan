from django.contrib import admin
from .models import Category, Article, Document, GalleryImage, TimelineEvent, UserProfile, Book


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name_odia', 'name_en', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name_en',)}
    search_fields = ['name_odia', 'name_en']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title_odia', 'title_en', 'category', 'is_featured', 'created_at']
    list_filter = ['category', 'is_featured', 'created_at']
    prepopulated_fields = {'slug': ('title_en',)}
    search_fields = ['title_odia', 'title_en', 'content_odia', 'content_en']
    ordering = ['-created_at']


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title_odia', 'title_en', 'category', 'file_type', 'download_count', 'is_active', 'uploaded_at']
    list_filter = ['category', 'is_active', 'uploaded_at']
    search_fields = ['title_odia', 'title_en', 'description_odia']
    ordering = ['-uploaded_at']


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['title_odia', 'title_en', 'is_featured', 'uploaded_at']
    list_filter = ['is_featured', 'uploaded_at']
    search_fields = ['title_odia', 'title_en', 'description_odia']
    ordering = ['-uploaded_at']


@admin.register(TimelineEvent)
class TimelineEventAdmin(admin.ModelAdmin):
    list_display = ['year', 'title_odia', 'title_en', 'order']
    list_filter = ['year']
    search_fields = ['title_odia', 'title_en', 'description_odia', 'description_en']
    ordering = ['year', 'order']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'joined_at']
    search_fields = ['user__username', 'user__email', 'phone']
    ordering = ['-joined_at']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title_odia', 'title_en', 'file_size', 'download_count', 'is_active', 'added_at']
    list_filter = ['is_active', 'added_at']
    search_fields = ['title_odia', 'title_en', 'description_odia', 'description_en']
    ordering = ['title_odia']
