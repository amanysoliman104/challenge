from django.conf.urls import url 
from app.api.views  import ( 
	CoffeeMachineAPIList , 
	CoffeePodAPIList , 
	CoffeeMachineAPISearch,
	CoffeePodAPISearch,
	)

urlpatterns = [ 
    url(r'machine$', CoffeeMachineAPIList.as_view()),
    url(r'pods$', CoffeePodAPIList.as_view()),
    url(r'search/machine/', CoffeeMachineAPISearch.as_view()),
    url(r'search/pods/', CoffeePodAPISearch.as_view()),
    
]
