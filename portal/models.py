from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """Category for organizing content"""
    name_odia = models.CharField(max_length=200, verbose_name="ନାମ (ଓଡ଼ିଆ)")
    name_en = models.CharField(max_length=200, blank=True, verbose_name="Name (English)")
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "ଶ୍ରେଣୀ"
        verbose_name_plural = "ଶ୍ରେଣୀଗୁଡ଼ିକ"
        ordering = ['name_odia']

    def __str__(self):
        return self.name_odia


class Article(models.Model):
    """Articles about Fakir Mohan Senapati's life, works, and legacy"""
    title_odia = models.CharField(max_length=300, verbose_name="ଶୀର୍ଷକ (ଓଡ଼ିଆ)")
    title_en = models.CharField(max_length=300, blank=True, verbose_name="Title (English)")
    slug = models.SlugField(unique=True)
    content_odia = models.TextField(verbose_name="ବିଷୟବସ୍ତୁ (ଓଡ଼ିଆ)")
    content_en = models.TextField(blank=True, verbose_name="Content (English)")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles', verbose_name="ଶ୍ରେଣୀ")
    image = models.ImageField(upload_to='articles/', blank=True, null=True, verbose_name="ଛବି")
    is_featured = models.BooleanField(default=False, verbose_name="ପ୍ରମୁଖ ଖବର")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="ସୃଷ୍ଟି ସମୟ")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="ଅପଡେଟ ସମୟ")

    class Meta:
        verbose_name = "ପ୍ରବନ୍ଧ"
        verbose_name_plural = "ପ୍ରବନ୍ଧଗୁଡ଼ିକ"
        ordering = ['-created_at']

    def __str__(self):
        return self.title_odia


class Document(models.Model):
    """Downloadable documents (PDFs) - Only for logged-in users"""
    title_odia = models.CharField(max_length=300, verbose_name="ଶୀର୍ଷକ (ଓଡ଼ିଆ)")
    title_en = models.CharField(max_length=300, blank=True, verbose_name="Title (English)")
    description_odia = models.TextField(blank=True, verbose_name="ବର୍ଣ୍ଣନା (ଓଡ଼ିଆ)")
    file = models.FileField(upload_to='documents/', verbose_name="ଫାଇଲ (PDF)")
    file_type = models.CharField(max_length=50, default='PDF', editable=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='documents', verbose_name="ଶ୍ରେଣୀ")
    download_count = models.PositiveIntegerField(default=0, verbose_name="ଡାଉନଲୋଡ ସଂଖ୍ୟା")
    is_active = models.BooleanField(default=True, verbose_name="ସକ୍ରିୟ")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="ଅପଲୋଡ ସମୟ")

    class Meta:
        verbose_name = "ଦଲିଲ"
        verbose_name_plural = "ଦଲିଲଗୁଡ଼ିକ"
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title_odia

    def increment_download_count(self):
        self.download_count += 1
        self.save()


class GalleryImage(models.Model):
    """Gallery images related to Fakir Mohan Senapati"""
    title_odia = models.CharField(max_length=200, verbose_name="ଶୀର୍ଷକ (ଓଡ଼ିଆ)")
    title_en = models.CharField(max_length=200, blank=True, verbose_name="Title (English)")
    description_odia = models.TextField(blank=True, verbose_name="ବର୍ଣ୍ଣନା (ଓଡ଼ିଆ)")
    image = models.ImageField(upload_to='gallery/', verbose_name="ଛବି")
    is_featured = models.BooleanField(default=False, verbose_name="ପ୍ରମୁଖ")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="ଅପଲୋଡ ସମୟ")

    class Meta:
        verbose_name = "ଗ୍ୟାଲେରୀ ଛବି"
        verbose_name_plural = "ଗ୍ୟାଲେରୀ ଛବିଗୁଡ଼ିକ"
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title_odia


class TimelineEvent(models.Model):
    """Timeline events for Fakir Mohan Senapati's life"""
    year = models.IntegerField(verbose_name="ବର୍ଷ")
    title_odia = models.CharField(max_length=300, verbose_name="ଶୀର୍ଷକ (ଓଡ଼ିଆ)")
    title_en = models.CharField(max_length=300, blank=True, verbose_name="Title (English)")
    description_odia = models.TextField(verbose_name="ବର୍ଣ୍ଣନା (ଓଡ଼ିଆ)")
    description_en = models.TextField(blank=True, verbose_name="Description (English)")
    order = models.PositiveIntegerField(default=0, verbose_name="କ୍ରମ")

    class Meta:
        verbose_name = "ସମୟରେଖା ଘଟଣା"
        verbose_name_plural = "ସମୟରେଖା ଘଟଣାବଳୀ"
        ordering = ['year', 'order']

    def __str__(self):
        return f"{self.year} - {self.title_odia}"


class UserProfile(models.Model):
    """Extended user profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=15, blank=True, verbose_name="ଫୋନ")
    bio = models.TextField(blank=True, verbose_name="ପରିଚୟ")
    joined_at = models.DateTimeField(auto_now_add=True, verbose_name="ସଦସ୍ୟତା ସମୟ")

    class Meta:
        verbose_name = "ବ୍ୟବହାରକାରୀ ପ୍ରୋଫାଇଲ"
        verbose_name_plural = "ବ୍ୟବହାରକାରୀ ପ୍ରୋଫାଇଲଗୁଡ଼ିକ"

    def __str__(self):
        return self.user.username


class Book(models.Model):
    """Books written by Fakir Mohan Senapati - Only for logged-in users"""
    title_odia = models.CharField(max_length=300, verbose_name="ଶୀର୍ଷକ (ଓଡ଼ିଆ)")
    title_en = models.CharField(max_length=300, blank=True, verbose_name="Title (English)")
    description_odia = models.TextField(blank=True, verbose_name="ବର୍ଣ୍ଣନା (ଓଡ଼ିଆ)")
    description_en = models.TextField(blank=True, verbose_name="Description (English)")
    file_path = models.CharField(max_length=500, verbose_name="ଫାଇଲ ପଥ")
    file_size = models.CharField(max_length=50, blank=True, verbose_name="ଫାଇଲ ଆକାର")
    download_count = models.PositiveIntegerField(default=0, verbose_name="ଡାଉନଲୋଡ ସଂଖ୍ୟା")
    is_active = models.BooleanField(default=True, verbose_name="ସକ୍ରିୟ")
    added_at = models.DateTimeField(auto_now_add=True, verbose_name="ଯୋଡ଼ାଯାଇଥିବା ସମୟ")

    class Meta:
        verbose_name = "ପୁସ୍ତକ"
        verbose_name_plural = "ପୁସ୍ତକଗୁଡ଼ିକ"
        ordering = ['title_odia']

    def __str__(self):
        return self.title_odia

    def increment_download_count(self):
        self.download_count += 1
        self.save()
