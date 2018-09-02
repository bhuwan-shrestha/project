from django.shortcuts import render
<<<<<<< HEAD
from webpage.models import BannerImage, HomeChoose, HomeService, ActionBtn, Testimonial, FeatureName, Social, AboutBanner, AboutDetails, OurTeam, ServiceBanner, ServiceDetails, FeatureCollection, ContactBanner, OfficeAddress, OfficeNumber, WorkingHours, InnerFeature, AuthorName, HouseDimenssion, ContactUs
from webpage.forms import ContactUsForm

=======
from webpage.models import BannerImage, HomeChoose, HomeService, ActionBtn, Testimonial, FeatureName, Social, AboutBanner, AboutDetails, OurTeam, ServiceBanner, ServiceDetails, FeatureCollection, ContactBanner, OfficeAddress, OfficeNumber, WorkingHours, ContactUs, InnerFeature
from webpage.forms import ContactUsForm

from django.shortcuts import get_object_or_404

>>>>>>> Pushing with Error
# Create your views here.
def index(request):
    banner_list = BannerImage.objects.all()
    feature_list = FeatureName.objects.all()
    choose_list = HomeChoose.objects.all()
    service_list = HomeService.objects.all()
    action = ActionBtn.objects.all()
    testimonial_list = Testimonial.objects.all()
    social_list = Social.objects.all()
    home_dict = {
        'banner_img': banner_list,
        'feature_listing' : feature_list,
        'choose_listing' : choose_list,
        'service_listing' : service_list,
        'actionbtn' : action,
        'testimonial_listing' : testimonial_list,
        'social_contact' : social_list,
    }
    return render(request, 'webpage/home.html', context=home_dict)

def about(request):
    about_banner = AboutBanner.objects.all()
    about_detail = AboutDetails.objects.all()
    our_team = OurTeam.objects.all()
    social_list = Social.objects.all()

    about_dict = {
        'abt_banner': about_banner,
        'about_details' : about_detail,
        'our_team' : our_team,
        'social_contact' : social_list,
    }

    return render(request, 'webpage/about-us.html', context= about_dict)

def services(request):
    service_banner = ServiceBanner.objects.all()
    service_details = ServiceDetails.objects.all()
    social_list = Social.objects.all()

    service_dict = {
        'service_banner': service_banner,
        'service_details': service_details,
        'social_contact' : social_list,
    }

    return render(request, 'webpage/services.html', context=service_dict)

def collection(request):
    feature_list = FeatureName.objects.all()
    feature_banner = FeatureCollection.objects.all()
    social_list = Social.objects.all()

    collection_dict = {
        'feature_listing' : feature_list,
        'feature_banner' : feature_banner,
        'social_contact' : social_list,
    }

    return render(request, 'webpage/feature-collection.html', context=collection_dict)

def contactPage(request):
    contact_banner = ContactBanner.objects.all()
    office_address = OfficeAddress.objects.all()
    office_number = OfficeNumber.objects.all()
    working_hour = WorkingHours.objects.all()
    social_list = Social.objects.all()
    form = ContactUsForm()

    contact_dict = {
        'contact_banner': contact_banner,
        'office_address': office_address,
        'office_number': office_number,
        'working_hour': working_hour,
        'social_contact' : social_list,
        'form' : form,
    }

<<<<<<< HEAD
    
=======

>>>>>>> Pushing with Error

    if request.method == "POST":
        form = ContactUsForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print('Error invalid form')

    return render(request, 'webpage/contact-us.html', context=contact_dict)



<<<<<<< HEAD
# def contactus(request):

    

#     return render(request, 'webpage/contact-us.html',{'form':form} )



def innerFeature(request):
    image_project = InnerFeature.objects.all()
    author_name = AuthorName.objects.all()
    house_area = HouseDimenssion.objects.all()
    social_list = Social.objects.all()

    inner_dict = {
        'image_project': image_project,
        'author_name': author_name,
        'house_area' : house_area,
        'social_contact' : social_list,
    }

=======
def innerFeature(request, pk):

    feature_list = InnerFeature.objects.all()
    # feature_name = get_object_or_404(FeatureName, pk=pk)
    social_list = Social.objects.all()

    inner_dict = {
        'feature_list': feature_list,
        # 'feature_name': feature_name,
        'social_contact' : social_list,
    }


>>>>>>> Pushing with Error
    return render(request, 'webpage/inner-feature.html', context=inner_dict)