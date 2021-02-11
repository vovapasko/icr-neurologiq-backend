from django.shortcuts import render
from django.views.generic import TemplateView
from ai.file_saver import file_saver


class ChoiseOfResultView(TemplateView):
    def post(self, request, *args, **kwargs):
        choices = request.POST.getlist('list')
        file_saver(choices)
        print(choices)
        context = {'choices': choices}
        return render(request, template_name='upload.html', context=context)
