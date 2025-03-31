from django.contrib import admin
from django.utils.html import format_html
from django.db import models
from django.forms import Textarea

from .models import Question  
from .models import MBTIDescriptionTrue
from .models import MBTISentenceTrue
from .models import MBTIDescriptionModified
from .models import MBTISentenceModified
from .models import MBTIVagueSentence
from .models import MBTIVagueBlock

@admin.register(MBTISentenceModified)
class MBTISentenceModifiedAdmin(admin.ModelAdmin):
    list_display = ('mbti_description', 'sentence', 'is_incorrect')  # 用 formatted_sentence 替换 sentence
    search_fields = ('sentence',)
    list_filter = ('is_incorrect',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'dimension')  # the text to be displayed in the list view at the admin panel
    search_fields = ('text',)             # allow searching by text field

@admin.register(MBTIDescriptionTrue)
class MBTIDescriptionAdmin(admin.ModelAdmin):
    list_display = ('mbti_type', 'description')
    search_fields = ('mbti_type',)


@admin.register(MBTISentenceTrue)
class MBTISentenceAdmin(admin.ModelAdmin):
    list_display = ('mbti_description', 'sentence', 'is_vague')
    list_filter = ('is_vague',)
    search_fields = ('sentence', 'mbti_description__mbti_type')


@admin.register(MBTIDescriptionModified)
class MBTIDescriptionModifiedAdmin(admin.ModelAdmin):
    list_display = ('mbti_type', 'description', 'wrong_mbti_type')
    search_fields = ('mbti_type',)

@admin.register(MBTIVagueSentence)
class MBTIVagueSentenceAdmin(admin.ModelAdmin):
    list_display = ('mbti_type', 'text')
    search_fields = ('mbti_type', 'text')

@admin.register(MBTIVagueBlock) 
class MBTIVagueBlockAdmin(admin.ModelAdmin):
    list_display = ('mbti_type', 'vague_text_block')
    search_fields = ('mbti_type', 'vague_text_block')

