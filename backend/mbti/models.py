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

     # Override the save method to split sentences into MBTISentenceTrue
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the MBTIDescriptionTrue instance first

        # Split the description text into individual sentences, keeping punctuation
        sentences = re.split(r'(?<=[.!?])(?=\s)', self.description)
        sentences = [s for s in sentences if s.strip()]  # filter out empty strings

        for sentence in sentences:
                MBTISentenceTrue.objects.update_or_create(
                    mbti_description=self,
                    sentence=sentence, 
                    defaults={'is_vague': False}  # Default to non-vague sentences
                )

       
class MBTISentenceTrue(models.Model):
    mbti_description = models.ForeignKey(MBTIDescriptionTrue, on_delete=models.CASCADE)
    sentence = models.TextField() 
    is_vague = models.BooleanField(default=False) 

    def __str__(self):
        return f'{self.mbti_description.mbti_type} - {self.sentence[:30]}'


class MBTIDescriptionModified(models.Model):
    mbti_type = models.CharField(max_length=4, unique=True) 
    description = models.TextField() 
    image = models.CharField(max_length=255) 
    wrong_mbti_type = models.CharField(max_length=4, blank=True)  # Incorrect MBTI type for the description
    def __str__(self):
        return self.mbti_type
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # save the MBTIDescriptionModified instance first

        # Split the description text into individual sentences, keeping punctuation
        sentences = re.split(r'(?<=[.!?])(?=\s)', self.description)
        sentences = [s for s in sentences if s.strip()]  # 过滤掉空字符串

        for sentence in sentences:
            # Check if the sentence exists in `MBTISentenceTrue` for the same MBTI type
            exists_in_true = MBTISentenceTrue.objects.filter(
                mbti_description__mbti_type=self.mbti_type,
                sentence__iexact=sentence  # ignore case for matching
            ).exists()

            # If the sentence does not exist, mark `is_incorrect = True`
            MBTISentenceModified.objects.update_or_create(
                mbti_description=self,
                sentence=sentence,
                defaults={'is_incorrect': not exists_in_true} 
            )


class MBTISentenceModified(models.Model):
    mbti_description = models.ForeignKey(MBTIDescriptionModified, on_delete=models.CASCADE) 
    sentence = models.TextField() 
    is_vague = models.BooleanField(default=False) 
    is_incorrect = models.BooleanField(default=False)
    correct_mbti_type = models.CharField(max_length=4, blank=True)  # Correct MBTI type for the incorrect description
        
    def __str__(self):
        return self.sentence
    def save(self, *args, **kwargs):
        # Ensure spaces and line breaks are not automatically removed when saving
        super().save(*args, **kwargs)


class MBTIVagueSentence(models.Model):
    mbti_type = models.CharField(max_length=4)
    text = models.CharField(max_length=255)  # Store vague phrases (e.g., "feel insecure")
    
    class Meta:
        unique_together = ('mbti_type', 'text')

    def __str__(self):
        return f"[{self.mbti_type}] {self.text[:30]}"
 

class MBTIVagueBlock(models.Model):
    """
    Each MBTI type corresponds to a block of vague text, with multiple phrases/segments separated by line breaks.
    Each line follows the format: sentence::explanation
    """
    mbti_type = models.CharField(max_length=4, unique=True)
    vague_text_block = models.TextField(
        help_text="Store multiple vague sentences with explanations, each line in the format: sentence::explanation"
    )

    def __str__(self):
        return f"{self.mbti_type}"

    def get_vague_list(self):
        """
        Split the entire block of text into a list of [{sentence: '...', explanation: '...'}].
        If a line does not contain the :: separator, the explanation defaults to an empty string.
        """
        lines = self.vague_text_block.split('\n')
        result = []
        for line in lines:
            line = line.strip()
            if not line:
                continue  # skip empty lines

            if '::' in line:
                # Split the line into sentence and explanation using '::' as the separator
                sentence, explanation = line.split('::', 1)
                result.append({
                    'sentence': sentence.strip(),
                    'explanation': explanation.strip()
                })
            else:
                # If no '::' separator is found, assume no explanation
                result.append({
                    'sentence': line,
                    'explanation': ''
                })

        return result




