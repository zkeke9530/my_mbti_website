# Route configuration
from django.urls import path
from .views import get_questions
from .views import submit_answers
from .views import get_mbti_description
from .views import get_full_mbti_description
from .views import get_mbti_description_modified
from .views import get_full_mbti_description_modified
from .views import get_vague_sentences_by_type
from .views import get_vague_sentences_block

urlpatterns = [
    path('questions/', get_questions, name='get_questions'), 
    path('submit/', submit_answers, name='submit_answers'),
    path('mbtiType/<str:mbtiType>/', get_mbti_description, name='get_mbti_description'),
    path('mbtiTypeFullDescription/<str:mbtiType>/', get_full_mbti_description, name='get_full_mbti_description'),
    path('mbtiTypeModified/<str:mbtiType>/', get_mbti_description_modified, name='get_mbti_description_modified'),
    path('mbtiTypeModifiedFullDescription/<str:mbtiType>/', get_full_mbti_description_modified, name='get_full_mbti_description_modified'),
    path('vagueSentences/<str:mbtiType>/', get_vague_sentences_by_type, name='get_vague_sentences_by_type'),
    path('vagueSentencesBlock/<str:mbtiType>/', get_vague_sentences_block, name='get_vague_sentences_block'),
]

