from django.shortcuts import render

def home(request):
    import json
    import requests

    if request.method=='POST':
        zipcode=request.POST['zipcode']
        apiadd=requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zipcode+"&distance=25&API_KEY=70044BF3-1269-4866-9021-F6AF4CAB2FAA")
        try:
            api = json.loads(apiadd.content)
        except Exception as e:
            api="Error"
        if api != "Error":
            if api[0]['Category']['Name']=="Good":
                category_discription="good"
                Category_color="good"
            elif api[0]['Category']['Name']=="Moderate":
                category_discription="Moderate"
                Category_color="Moderate"
            elif api[0]['Category']['Name']=="Unhealthy for Sensitive Groups (USG)":
                category_discription="Unhealthy"
                Category_color="Unhealthy for Sensitive Groups (USG)"
            elif api[0]['Category']['Name']=="Unhealthy":
                category_discription="Unhealthy"
                Category_color="Unhealthy"
            elif api[0]['Category']['Name']=="Very Unhealthy":
                category_discription="Very Unhealthy"
                Category_color="Very Unhealthy"
            elif api[0]['Category']['Name']=="Hazardous":
                category_discription="Hazardous"
                Category_color="Hazardous"

        return render(request, 'home.html', {'api': api,
                           'category_discription':category_discription,
                           'Category_color':Category_color},)


    else:
        apiadd=requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=85001&distance=25&API_KEY=70044BF3-1269-4866-9021-F6AF4CAB2FAA")
        try:
            api = json.loads(apiadd.content)
        except Exception as e:
            api = "Error"
            if api!="Error":
                if api[0]['Category']['Name']=="Good":
                    category_discription="good"
                    Category_color="good"
                elif api[0]['Category']['Name']=="Moderate":
                    category_discription="Moderate"
                    Category_color="Moderate"
                elif api[0]['Category']['Name']=="Unhealthy for Sensitive Groups (USG)":
                    category_discription="Unhealthy for Sensitive Groups (USG)"
                    Category_color="Unhealthy for Sensitive Groups (USG)"
                elif api[0]['Category']['Name']=="Unhealthy":
                    category_discription="Unhealthy"
                    Category_color="Unhealthy"
                elif api[0]['Category']['Name']=="Very Unhealthy":
                    category_discription="Very Unhealthy"
                    Category_color="Very Unhealthy"
                elif api[0]['Category']['Name']=="Hazardous":
                    category_discription="Hazardous"
                    Category_color="Hazardous"

        return render(request, 'home.html', {'api':api,
                           'category_discription':category_discription,
                           'Category_color':Category_color})


def about(request):
    return render(request, 'about.html', {})
