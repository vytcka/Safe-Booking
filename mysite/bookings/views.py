from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.urls import path
from django.test import SimpleTestCase, override_settings



def home(request):
    return HttpResponse("Welcome to the shop")
        
def menuPage(request):
    return HttpResponse("")
def response_error_handler(request, exception = None):
    return HttpResponse("Error handler content", status= (403))

def premission_denied(request):
    return PermissionDenied


handler403 = response_error_handler

def members(request):
    return HttpResponse("")

@override_settings(ROOT_URLCONF=__name__)
class CustomErrorHandlerTests(SimpleTestCase):
    def test_handler_renders_template_response(self):
        response = self.client.get("/403/")
        self.assertContains(response, "Error handler content", status_code=403)