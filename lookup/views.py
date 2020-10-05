from django.shortcuts import render
import json
import requests
import pgeocode
nomi = pgeocode.Nominatim('IN')


def home(request):
    if request.method=='POST':
        zipcode=request.POST['zipcode']
        latt=nomi.query_postal_code(zipcode).latitude
        longg=nomi.query_postal_code(zipcode).longitude   
        apiadd=requests.get("http://api.airvisual.com/v2/nearest_city?lat={}&lon={}&key=ba3a884e-9835-4c7b-bfe5-b5965d9b0dae".format(latt,longg))     
        apiadd.raise_for_status()
        try:
            api = apiadd.json()
        except:
            api="Error"  
        if api !="Error":
            value=api["data"]["current"]["pollution"]["aqius"]
            if value<=50:
                category_discription="good"
                Category_color="good"
            elif value<=100:
                category_discription="Moderate"
                Category_color="Moderate"
            elif value<=150:
                category_discription="Unhealthy"
                Category_color="Unhealthy for Sensitive Groups (USG)"
            elif value<=200:
                category_discription="Unhealthy"
                Category_color="Unhealthy"
            elif value<=300:
                category_discription="Very Unhealthy"
                Category_color="Very Unhealthy"
            elif value<=500:
                category_discription="Hazardous"
                Category_color="Hazardous"

        return render(request, 'home.html', {'api': api,
                           'category_discription':category_discription,
                           'Category_color':Category_color,'Zipcode':zipcode})

    else:
        apiadd=requests.get("http://api.airvisual.com/v2/nearest_city?lat=26.8717&lon=81.0729&key=ba3a884e-9835-4c7b-bfe5-b5965d9b0dae")
        apiadd.raise_for_status()
        try:
            api =apiadd.json()
        except:
            api="Error"
        category_discription="good"
        Category_color="good"    
        if api != "Error":
            value=api["data"]["current"]["pollution"]["aqius"]
            if value<=50:
                category_discription="good"
                Category_color="good"
            elif value<=100:
                category_discription="Moderate"
                Category_color="Moderate"
            elif value<=150:
                category_discription="Unhealthy"
                Category_color="Unhealthy for Sensitive Groups (USG)"
            elif value<=200:
                category_discription="Unhealthy"
                Category_color="Unhealthy"
            elif value<=300:
                category_discription="Very Unhealthy"
                Category_color="Very Unhealthy"
            elif value<=500:
                category_discription="Hazardous"
                Category_color="Hazardous"

        return render(request, 'home.html', {'api': api,
                           'category_discription':category_discription,
                           'Category_color':Category_color})

def about(request):
    return render(request, 'about.html', {})
