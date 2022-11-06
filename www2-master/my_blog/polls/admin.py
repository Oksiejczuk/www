from django.contrib import admin
from .models import Question, Choice

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date',)
    list_filter = ('question_text','pub_date',)
    search_fields = ('question_text',)
@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
   list_display = ('get_question', 'choice_text', 'votes')
   list_filter = ('question', 'votes',)
   search_fields = ('choice_text', 'question__question_text',)
   raw_id_fields = ('question',)

   @admin.display(description='Question text', )
   def get_question(self, obj):
       return obj.question.question_text