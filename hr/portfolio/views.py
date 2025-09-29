from django.shortcuts import render
from django.http import JsonResponse
from .models import Contact

def home(request):
    return render(request, "index.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if not (name and email and message):
            return JsonResponse({"status": "error", "message": "All fields required"}, status=400)

        Contact.objects.create(name=name, email=email, message=message)

        return JsonResponse({"status": "success", "message": "Message saved!"})

    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)
