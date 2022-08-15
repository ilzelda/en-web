from django.shortcuts import render, redirect, get_object_or_404
from .forms import DiaryForm
from .models import Diary
from django.utils import timezone

# Create your views here.
def showDiaryList(request):
    diaries = Diary.objects.filter().order_by('date')
    return render(request, 'diary_list.html', {'diaries':diaries})

def createNewDiary(request):
    if request.method == "POST":
        form = DiaryForm(request.POST)
        if form.is_valid():
            new_diary = Diary()
            new_diary.date = form.cleaned_data['date']
            new_diary.description = form.cleaned_data['description']
            new_diary.save()

            return redirect('diary')
    else :
        form = DiaryForm()
        return render(request, 'new_diary.html', {'form':form})    

def updateDiary(request, diary_id):
    diary = get_object_or_404(Diary, pk=diary_id)
    return render(request, 'update_diary.html', {'diary':diary})

