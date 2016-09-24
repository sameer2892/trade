import requests
import json
# from django.shortcuts import render
from django.http import HttpResponse
from tradeapp.views.utils import views_utils


def read_json(request):

    # url = "http://api.geonames.org/citiesJSON?north=44.1&south=-9.9&east=-22.4&west=55.2&lang=de&username=demo"
    url = "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/ajaxGetQuoteJSON.jsp?symbol=sbin"
    response = requests.request("GET", url)
    print response
    data = json.loads(response.text)

    data1= views_utils.get_dict_for_loop(data)



    # return render(request, 'tradeapp/json.html', {'data1': data})
    return HttpResponse(json.dumps(data1), content_type="application/json")
    # print data1111










# url = "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/ajaxGetQuoteJSON.jsp?symbol=sbin"

# querystring = {"symbol":"sbin"}

# headers = {
#     'cache-control': "no-cache",
#     'postman-token': "7ef6193b-83b9-cd7b-0c5d-36d6c2a2e7c5"
#     }

# response = requests.request("GET", url)
# print "-------------------------"
# print type(response)
