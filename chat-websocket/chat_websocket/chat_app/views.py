from django.shortcuts import render
from .models import chatmsgs
# Create your views here.
def get(request):
    queryset = chatmsgs.objects.all()
    print(queryset)
    # if request.method == "POST":
    context = {"object_list" : queryset}
    return render(request, 'chat_list.html',context)
