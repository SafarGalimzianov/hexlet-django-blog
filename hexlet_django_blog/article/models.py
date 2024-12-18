from django.db import models

# Create your models here.

# базовая модель для наследования
class Article(models.Model):
    # Атрибут - столбец таблицы
    name = models.CharField(max_length=200) # VARCHAR(200)
    body = models.TextField() #TEXT
    # Незименяемая временная метка
    created_at = models.DateTimeField(auto_now_add=True) # Не меняется после создания (CREATE)
    # Изменяемая временная метка
    updated_at = models.DateTimeField(auto_now=True) # Меняется после CREATE (UPDATE и при сохранении модели)
