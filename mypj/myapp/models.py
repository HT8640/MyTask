from django.db import models

class AnalysisLog(models.Model):
    image_path = models.CharField('画像ファイルのPath', max_length=255)
    success = models.CharField('成否', max_length=255)
    message = models.CharField('メッセージ', max_length=255)
    data_class = models.IntegerField('クラス', db_column='class')
    confidence = models.DecimalField('信頼度', max_digits=5, decimal_places=4)
    request_timestamp = models.IntegerField('リクエストタイムスタンプ')
    response_timestamp = models.IntegerField('レスポンスタイムスタンプ')
    
    class Meta:
        db_table = 'ai_analysis_log'
    
    def __str__(self):
        return f'{self.image_path}({self.request_timestamp})'