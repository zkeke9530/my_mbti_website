# 处理 MBTI 逻辑的视图函数
# 提供 API 接口：
# 获取问题列表：返回所有问题。
# 接收用户答案：计算 MBTI 结果并返回对应描述

# api_view这个工具把普通的函数变成可以处理 API 请求的函数，同时你可以指定它只接受某些请求方式，比如 GET
# 这个函数只能处理 GET 请求
# 比如用户通过浏览器直接访问 URL，
# 或者前端通过 axios.get 发送请求

from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Question
from .models import MBTIDescriptionTrue
from .models import MBTISentenceTrue
from .models import MBTIDescriptionModified
from .models import MBTISentenceModified
from .models import MBTIVagueSentence
from .models import MBTIVagueBlock
from .serializers import QuestionSerializer
from .serializers import MBTIDescriptionSerializer
import collections
import re

@api_view(['GET'])
def get_questions(request):
    questions = Question.objects.all()
    data = [
        {
            'id': question.id, 
            'text': question.text,
            'dimension': question.dimension,
            'options': [
                {'text': question.option_1, 'weight': question.weight_1},
                {'text': question.option_2, 'weight': question.weight_2},
                {'text': question.option_3, 'weight': question.weight_3},
                {'text': question.option_4, 'weight': question.weight_4},
                {'text': question.option_5, 'weight': question.weight_5},
            ]
        }
        for question in questions
    ]
    return Response(data)


@api_view(['POST'])
def submit_answers(request):
    answers = request.data.get('answers', [])
    mbti_type = request.data.get('mbtiType', 'Unknown')
    
    # 模拟计算分数逻辑，这里直接返回前端传来的类型
    return Response({
        'mbtiType': mbti_type
    })


# # 获取 MBTI 描述的 API
# @api_view(['GET'])
# def get_mbti_description(request, mbtiType):
#     try:
#         mbti_desc = MBTIDescription.objects.get(mbti_type=mbtiType)
#         serializer = MBTIDescriptionSerializer(mbti_desc)
#         # 拼接完整的静态路径，确保前端可以加载到图片
#         data = serializer.data
#         data['image'] = f"{settings.STATIC_URL}{data['image']}"
#         return Response(data)
#     except MBTIDescription.DoesNotExist:
#         return Response({
#             'error': '描述未找到',
#             'image': f"{settings.STATIC_URL}images/default.png"
#         }, status=404)
    
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MBTIDescriptionTrue, MBTISentenceTrue

@api_view(['GET'])
def get_mbti_description(request, mbtiType):
    try:
        mbti_desc = MBTIDescriptionTrue.objects.get(mbti_type=mbtiType)
        sentences = MBTISentenceTrue.objects.filter(mbti_description=mbti_desc)

        data = {
            'mbti_type': mbti_desc.mbti_type,
            'description': [
                {'sentence': s.sentence, 'is_vague': s.is_vague} for s in sentences
            ],
            'image': mbti_desc.image
        }
        return Response(data)
    except MBTIDescriptionTrue.DoesNotExist:
        return Response({'error': '描述未找到'}, status=404)


@api_view(['GET'])
def get_full_mbti_description(request, mbtiType):
    try:
        mbti_desc = MBTIDescriptionTrue.objects.get(mbti_type=mbtiType)
        data = {
            'mbti_type': mbti_desc.mbti_type,
            'description': mbti_desc.description,
            'image': mbti_desc.image
        }
        return Response(data)
    except MBTIDescriptionTrue.DoesNotExist:
        return Response({'error': '描述未找到'}, status=404)
    
    
@api_view(['GET'])
def get_mbti_description_modified(request, mbtiType):
    try:
        mbti_desc = MBTIDescriptionModified.objects.get(mbti_type=mbtiType)
        wrong_mbti_type = MBTIDescriptionModified.objects.get(mbti_type=mbtiType).wrong_mbti_type
        sentences = MBTISentenceModified.objects.filter(mbti_description=mbti_desc)

        data = {
            'mbti_type': mbti_desc.mbti_type,
            'description': [
                {'sentence': s.sentence, 'is_incorrect': s.is_incorrect} for s in sentences
            ],
            'image': mbti_desc.image,
            'wrong_mbti_type': mbti_desc.wrong_mbti_type 
        }
        return Response(data)
    except MBTIDescriptionModified.DoesNotExist:
        return Response({'error': '描述未找到'}, status=404)
    

@api_view(['GET'])
def get_full_mbti_description_modified(request, mbtiType):
    try:
        mbti_desc = MBTIDescriptionModified.objects.get(mbti_type=mbtiType)
        data = {
            'mbti_type': mbti_desc.mbti_type,
            'description': mbti_desc.description,  # 假设 description 字段包含完整的描述文本
            'image': mbti_desc.image,
            'wrong_mbti_type': mbti_desc.wrong_mbti_type
        }
        return Response(data)
    except MBTIDescriptionModified.DoesNotExist:
        return Response({'error': '描述未找到'}, status=404)
    

@api_view(['GET'])
def get_vague_sentences_by_type(request, mbtiType):
 
    # 返回给定 mbti_type 的所有“模糊”句子列表
    # 示例：GET /api/vagueSentences/INFP/
 
    vague_list = MBTIVagueSentence.objects.filter(mbti_type=mbtiType).values_list('text', flat=True)
    return Response(list(vague_list))

# @api_view(['GET'])
# def get_vague_sentences_block(request, mbtiType):
#     """
#     示例: GET /api/vagueBlock/INFP/
#     返回一个字符串数组，每个元素是换行拆分后的短语
#     """
#     try:
#         block_obj = MBTIVagueBlock.objects.get(mbti_type=mbtiType)
#         lines = block_obj.get_vague_list()  # 拆分成列表
#         return Response(lines)
#     except MBTIVagueBlock.DoesNotExist:
#         return Response([], status=200)  # 如果找不到，就返回空列表

@api_view(['GET'])
def get_vague_sentences_block(request, mbtiType):
    try:
        block_obj = MBTIVagueBlock.objects.get(mbti_type=mbtiType)
        # 假设 get_vague_list() 已经返回 [{sentence: '...', explanation: '...'}, ...]
        data = block_obj.get_vague_list()
        return Response(data)
    except MBTIVagueBlock.DoesNotExist:
        return Response([], status=200)


import random
from django.shortcuts import render, get_object_or_404


def show_mbti_description(request, mbti_type):
    # 获取 A 型的正确描述对象
    description_true = get_object_or_404(MBTIDescriptionTrue, mbti_type=mbti_type)
    # 获取所有正确的句子（列表）
    original_sentences = list(MBTISentenceTrue.objects.filter(mbti_description=description_true))
    
    # 设定替换数量，比如替换2个句子
    replacement_count = 2
    
    # 假设错误描述中 wrong_mbti_type 指定了要替换成哪个类型（例如 'B'）
    # 这里我们先尝试获取 MBTIDescriptionModified 中 mbti_type 为 A 且 wrong_mbti_type 为 B 的对象
    wrong_type = 'B'  # 你可以根据需要调整
    try:
        description_modified = MBTIDescriptionModified.objects.get(mbti_type=mbti_type, wrong_mbti_type=wrong_type)
        # 获取所有错误的句子，并且标记为错误的（is_incorrect=True）
        candidate_replacements = list(MBTISentenceModified.objects.filter(mbti_description=description_modified, is_incorrect=True))
    except MBTIDescriptionModified.DoesNotExist:
        candidate_replacements = []
    
    # 如果候选句子足够，则随机抽取 replacement_count 个
    if candidate_replacements:
        num_replacements = min(replacement_count, len(candidate_replacements))
        replacements = random.sample(candidate_replacements, num_replacements)
        # 从原始句子中随机选择几个索引来替换
        if len(original_sentences) >= num_replacements:
            indices_to_replace = random.sample(range(len(original_sentences)), num_replacements)
            for i, index in enumerate(indices_to_replace):
                # 这里直接替换整个对象（你可以选择只替换句子文本）
                original_sentences[index] = replacements[i]
    
    context = {
        'mbti_type': mbti_type,
        'sentences': original_sentences,  # 替换后的句子列表
        'description_image': description_true.image,
    }
    
    return render(request, 'mbti_display.html', context)
