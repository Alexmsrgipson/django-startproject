from django import template

register = template.Library()


# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def censor(value):
   bed = ['Редиска', 'дурак']

   value.split(" ")


   newtext = value.split(" ")

   for int in range(len(newtext)):
      # для списка плохих слов
      for i in bed:
         if i == newtext[int]:
            newtext[int] = "***"



   return f'{" ".join(newtext)} '