from django.shortcuts import get_object_or_404, render
from django.core.mail import send_mail
from .models import CarouselImage
from django.urls import reverse
from django.views import generic
from django.contrib.sitemaps import Sitemap
#from website.models import Content

customer_info = {
    "cName": "A N A S S E",
    "cSlogan": "Hotelservice & Dienstleistungen",
    "cInH": "InH. Anasse Boukari",
    "cAddr": "Koblenzer straße 31",
    "cPLZ": "60327",
    "cCity": "Frankfurt am Main",
    "cState": "Hessen",
    "cTel": "+49 176 638 993 63",
    "cOpnMn": "Mon-DO: 09:00 bis 18:00 Uhr",
    "cOpnFr": "FR: 09:00 bis 15:00 Uhr",
    "message_name": "message_name",
    "cWebsite": "https://anasse.de",
    "cEmail": "info@anasse.de",
    "cQuestions": "Noch Fragen?", #"Have a Questions?",
    "cOpenHrs": "Geschäftszeiten",
    "cOpenDays": "Öffnungstage:",
    "cEmergency": "Für Notfälle",
    "cVaccation": "Ferien",
    "cWorks": "Die Art von Arbeiten, die wir ausführen",
    "cSubheading": "Sauber Räume, glückliche Gesichter",
    "cFriendly": "Wir verwenden umweltfreundliche Reinigungsprodukte für Kunden, die ökologische Reinigungslösungen bevorzugen.",
    "cMission": "Unsere Mission ist es, das vertrauenswürdigste und zuverlässigste Reinigungsunternehmen in der Region zu werden. Wir werden dies erreichen, indem wir außergewöhnliche Reinigungsdienste anbieten, umweltfreundliche Reinigungsprodukte verwenden und wettbewerbsfähige Preise anbieten.",
    "cQLinks":"Quick Links",
    "cNHome":"Willkommen",
    "cNAbout":"Über uns",
    "cNServices":"Dienstleistung",
    "cNBlog":"Stellenangebote",
    "cNContact":"Kontakt",
    "cSOffice":"GEBÄUDEREINIGUNG",
    "cSOfficeSl":"Wir stellen Ihnen kompetente Mitarbeiter zur Verfügung. Sei es für Grundreinigungen oder den täglichen Bedarf.Unterhaltsreinigung, Büroreinigung, Wellness- und Spa- Bereiche,Glasreinigung, Teppichreinigung / Shampoonierarbeiten",
    "cSKitchen":"STEWARDING",
    "cSKitchenSl":"Die Küche bedarf der ständigen Beobachtung hinsichtlich Qualität und Kosten. Die Entlastung in der Personal disposition ermöglicht Ihnen die Konzentration auf IHR Kerngeschäft. Wir sind in diesem Bereich Ihr Ansprechpartner und zeichnen uns aus durch langjährige Erfahrung und Kompetenz.",
    "cSRezeption":"Rezeption",
    "cSRezeptionSl":"Ein freundlicher und kompetenter Empfang ist der Schlüssel eines gastfreundlichen Hauses, hier bieten Wir Ihnen passendes Personal um Ihren Standard zu gewährleisten. Sprechen Sie uns an.",
    "cSService":"Service",
    "cSServiceSl":"Dienstleistung ist unsere Leidenschaft! Sei es im Restaurantservice, Bankett oder Gala wir bieten Ihnen die passenden kooperations- Möglichkeiten",
    "cSHousekeep":"Housekeeping",
    "cSHousekeepSl":"Two smiling cleaners cleaning room together Anasse Hotelservice steht für Reinigungsarbeiten der extra klasse! Zimmereinigung Bereitstellung von Hausdamen Minibar service Abdeckservice/ Turndown Betten und Wäschedienste Matratzenreinigung Pflege von Public Areas und Außenanlagen Konferenzservice Vorarbeiter zur Einarbeitung Allgemeiner ersonalservice Im allgemeinen bieten wir Ihnen folgende Dienstleistungen, hier unsere Leistungen im Überblick:",
    "cSCatering":"Catering",
    "cSCateringSl":"Bankett- und Konferenzservice Personaldienste Empfangsservice Post- und Botendienste Schmutzfangmattenservice Hausmeisterservice",
        
}
# Create your views here.
class IndexView(generic.ListView):
    template_name = "test.html"
    context_object_name = "latest_question_list"
    
def index(request):
    return render(request, 'index.html', customer_info)

def about(request):
    return render(request, 'about.html', customer_info)

def services(request):
    return render(request, 'services.html', customer_info)

def portfolio(request):
    return render(request, 'portfolio.html', customer_info)

def pricing(request):
    return render(request, 'pricing.html', customer_info)

def blog(request):
    return render(request, 'stellenangebote.html', customer_info)

def carousel(request):
    images = CarouselImage.objects.all()
    #a = {'carousel_images': carousel_images}
    #context = customer_info.values.__new__(a.values)
    #context = {'customer_info': customer_info, 'carousel_images': carousel_images}
    return render(request, 'carousel.html', {'carousel_images': images})
    #return render(request, 'carousel.html', context)

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        
        # send an email
        send_mail(
            message_name, # subject
            message, # message
            message_email, # from email
            ['receiver@domain.com'] # to email
            
        )
        
        return render(request, 'kontakt.html', customer_info)
    
    else:
        return render(request, 'kontakt.html', customer_info)

def appointment(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        
        # send an email
        send_mail(
            message_name, # subject
            message, # message
            message_email, # from email
            ['receiver@domain.com'] # to email
            
        )
        
        return render(request, 'appointment.html', {'message_name': message_name})
    
    else:
        return render(request, 'home.html', customer_info)