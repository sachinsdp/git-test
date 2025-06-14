from django.http import HttpResponse

def show_data(request):
    return HttpResponse(f"Text file content: {request.db_data}")
