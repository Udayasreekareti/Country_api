from django.shortcuts import render
import requests
def index(request): 
    response = requests.get("https://restcountries.com/v2/all") 
    all_countries = response.json() 
    query = request.GET.get('query') # Get the search query from the request 
    data = [] 
    if query: 
           for country in all_countries: 
            if query.lower() in country['name'].lower(): 
                data.append({ 'name': country['name'], 'capital': country.get('capital', 'N/A'), 'region': country.get('region', 'N/A'), 'subregion': country.get('subregion', 'N/A'), 'languages': [lang['name'] for lang in country.get('languages', [])], 'calling_code': country.get('callingCodes', ['N/A'])[0], 'borders': country.get('borders', []), 'latlng': country.get('latlng', []), 'population': country.get('population', 'N/A'), 'area': country.get('area', 'N/A'), 'flag': country.get('flag', 'N/A'), 'currency_symbol': country.get('currencies', [{'symbol': 'N/A'}])[0].get('symbol', 'N/A') })
    else: 
        for country in all_countries: 
            data.append({ 'name': country['name'], 'capital': country.get('capital', 'N/A'), 'region': country.get('region', 'N/A'), 'subregion': country.get('subregion', 'N/A'), 'languages': [lang['name'] for lang in country.get('languages', [])], 'calling_code': country.get('callingCodes', ['N/A'])[0], 'borders': country.get('borders', []), 'latlng': country.get('latlng', []), 'population': country.get('population', 'N/A'), 'area': country.get('area', 'N/A'), 'flag': country.get('flag', 'N/A'), 'currency_symbol': country.get('currencies', [{'symbol': 'N/A'}])[0].get('symbol', 'N/A') })    
    return render(request, 'index.html', {'data':data})