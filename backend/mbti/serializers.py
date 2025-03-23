# 数据序列化，用于 API 返回 JSON
# 将问题和结果数据转换成 JSON 格式，供前端调用
# from rest_framework import serializers
# from .models import Question

# class QuestionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Question
#         fields = '__all__'  # 序列化所有字段

from rest_framework import serializers
from .models import Question
from .models import MBTIDescriptionTrue

class QuestionSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()  # 添加自定义字段

    class Meta:
        model = Question
        fields = ['text', 'dimension', 'options']  # 指定返回的字段

    # 自定义方法，返回选项数组
    def get_options(self, obj):
        return obj.options()  # 调用模型中的 options 方法

class MBTIDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MBTIDescriptionTrue
        fields = '__all__'

