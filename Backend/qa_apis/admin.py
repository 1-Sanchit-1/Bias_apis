from django.contrib import admin
from .models import PDFFile,QuestionAnswer

@admin.register(PDFFile)
class PDFFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at')



@admin.register(QuestionAnswer)
class PDFFileAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')