from django.test import Client
from search_engine.templates import form
from search_engine.views import formpage

def testfrom():
    c = Client()
    response = c.post('/form',{"type": "Kino", "name": "Multikino", "district": "Śródmieście", "address": "Jana Pawła II"})
    assert response.status_code == 200