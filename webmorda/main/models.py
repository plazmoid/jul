from django.db.models import *


# Страница конкретного опросника
class QuizSelect(Model):
    # идентификатор страницы опросника
    internal_name = CharField(
        primary_key=True, max_length=50, default="no_name")
    name = CharField(max_length=50)


# Элемент выпадающего списка
class QuizItem(Model):
    id = IntegerField(primary_key=True)
    value = CharField(max_length=50)


# Таблица сопоставления элементов списка и самого списка
class QuizRules(Model):
    page_name = ForeignKey(QuizSelect, on_delete=CASCADE)
    item = ForeignKey(QuizItem, on_delete=CASCADE)
    # строка вида '1,2,3', где цифры - QuizItem.id
    # если ранее были выбраны элементы любого выпадающего списка, id который есть в этой строке, данный элемент будет виден
    show_if = CharField(max_length=200)
