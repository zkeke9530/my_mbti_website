from django.db import models


class Question(models.Model):
    text = models.CharField(max_length=255)
    dimension = models.CharField(
        max_length=2,
        choices=[
            ('EI', 'extraverted(E) / introverted(I)'),
            ('SN', 'sensing(S) / intuition(N)'),
            ('TF', 'thinking(T) / feeling(F)'),
            ('JP', 'judgement(J) / perception(P)'),
        ]
    )
    
    option_1 = models.CharField(max_length=100, default="Strongly Disagree")
    option_2 = models.CharField(max_length=100, default="Disagree")
    option_3 = models.CharField(max_length=100, default="Neutral")
    option_4 = models.CharField(max_length=100, default="Agree")
    option_5 = models.CharField(max_length=100, default="Strongly Agree")

    # every question has a weight for each option, may be different
    weight_1 = models.IntegerField(default=1)
    weight_2 = models.IntegerField(default=2)
    weight_3 = models.IntegerField(default=3)
    weight_4 = models.IntegerField(default=4)
    weight_5 = models.IntegerField(default=5)

    def __str__(self):
        return self.text


import re   # regular expression module

class MBTIDescriptionTrue(models.Model):
    mbti_type = models.CharField(max_length=4, unique=True) 
    description = models.TextField()
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.mbti_type

    # 重写 save 方法，实现同步拆分句子到 MBTISentenceTrue
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # 先保存 MBTIDescriptionTrue 实例

        # 拆分描述文本为单句，并保留标点符号
        sentences = re.split(r'(?<=[.!?])(?=\s)', self.description)
        sentences = [s for s in sentences if s.strip()]  # 过滤掉空字符串

        for sentence in sentences:
                MBTISentenceTrue.objects.update_or_create(
                    mbti_description=self,
                    sentence=sentence, 
                    defaults={'is_vague': False}  # 默认为非模糊语句
                )

       
class MBTISentenceTrue(models.Model):
    mbti_description = models.ForeignKey(MBTIDescriptionTrue, on_delete=models.CASCADE)
    sentence = models.TextField()  # MBTI 具体的句子
    is_vague = models.BooleanField(default=False)  # 句子是否模糊，默认为 False

    def __str__(self):
        return f'{self.mbti_description.mbti_type} - {self.sentence[:30]}'


class MBTIDescriptionModified(models.Model):
    mbti_type = models.CharField(max_length=4, unique=True)  # MBTI 类型
    description = models.TextField()  # MBTI 描述
    image = models.CharField(max_length=255)  # 图片路径存储
    wrong_mbti_type = models.CharField(max_length=4, blank=True)  # 错误描述属于的MBTI 类型

    def __str__(self):
        return self.mbti_type
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # 先保存 MBTIDescriptionModified 实例

        # 拆分描述文本为单句，并保留标点符号
        sentences = re.split(r'(?<=[.!?])(?=\s)', self.description)
        sentences = [s for s in sentences if s.strip()]  # 过滤掉空字符串

        for sentence in sentences:
            # 检查 `MBTISentenceTrue` 是否有相同的句子（同一个 MBTI 类型下）
            exists_in_true = MBTISentenceTrue.objects.filter(
                mbti_description__mbti_type=self.mbti_type,
                sentence__iexact=sentence  # 忽略大小写
            ).exists()


            # 如果找不到相同的句子，则 `is_incorrect = True`
            MBTISentenceModified.objects.update_or_create(
                mbti_description=self,
                sentence=sentence,
                defaults={'is_incorrect': not exists_in_true}  # 句子不存在则标记为错误
            )


class MBTISentenceModified(models.Model):
    mbti_description = models.ForeignKey(MBTIDescriptionModified, on_delete=models.CASCADE)  # 关联的 MBTI 描述
    sentence = models.TextField()  # 单句描述
    is_vague = models.BooleanField(default=False)  # 是否是模糊描述
    is_incorrect = models.BooleanField(default=False)  # 是否是错误描述
    correct_mbti_type = models.CharField(max_length=4, blank=True)  # 错误描述应属于的正确 MBTI 类型
        
    def __str__(self):
        return self.sentence
    def save(self, *args, **kwargs):
        # 确保保存时不自动去除空格和换行
        super().save(*args, **kwargs)


class MBTIVagueSentence(models.Model):
    mbti_type = models.CharField(max_length=4)
    text = models.CharField(max_length=255)  # 存储模糊短语（例如： "feel insecure" ）
    
    class Meta:
        unique_together = ('mbti_type', 'text')

    def __str__(self):
        return f"[{self.mbti_type}] {self.text[:30]}"
 
# class MBTIVagueBlock(models.Model):
#     """
#     一个 MBTI 类型对应一整段模糊文本，以换行分割多个短语/片段。
#     """
#     mbti_type = models.CharField(max_length=4, unique=True)
#     vague_text_block = models.TextField(
#         help_text="Store multiple vague sentences separated by line breaks"
#     )

#     def __str__(self):
#         return f"{self.mbti_type}"

#     def get_vague_list(self):
#         """
#         将整个换行文本拆分为列表并去除空行
#         """
#         lines = self.vague_text_block.split('\n')
#         lines = [line.strip() for line in lines if line.strip()]
#         return lines

class MBTIVagueBlock(models.Model):
    """
    一个 MBTI 类型对应一整段模糊文本，以换行分割多个短语/片段。
    每行的格式是：句子::解释
    """
    mbti_type = models.CharField(max_length=4, unique=True)
    vague_text_block = models.TextField(
        help_text="Store multiple vague sentences with explanations, each line in the format: sentence::explanation"
    )

    def __str__(self):
        return f"{self.mbti_type}"

    def get_vague_list(self):
        """
        将整个换行文本拆分为 [{sentence: '...', explanation: '...'}] 的列表
        如果某行没有 :: 分隔符，则解释部分默认为空字符串
        """
        lines = self.vague_text_block.split('\n')
        result = []
        for line in lines:
            line = line.strip()
            if not line:
                continue  # 跳过空行

            if '::' in line:
                # 以 '::' 为分隔符拆分出句子和解释
                sentence, explanation = line.split('::', 1)
                result.append({
                    'sentence': sentence.strip(),
                    'explanation': explanation.strip()
                })
            else:
                # 如果没有 '::' 分隔符，就默认没有解释
                result.append({
                    'sentence': line,
                    'explanation': ''
                })

        return result




