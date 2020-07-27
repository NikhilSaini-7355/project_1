from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
import requests
import json
import pyttsx3
engine = pyttsx3.init()

news1 = requests.get("https://newsapi.org/v2/top-headlines?country=in&apikey=073c51d8af8f4ba88159626447b71cdb")
api1 = json.loads(news1.content)
news2 = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=science&apikey=073c51d8af8f4ba88159626447b71cdb")
api2 = json.loads(news2.content)

news3 = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=sports&apikey=073c51d8af8f4ba88159626447b71cdb")
api3 = json.loads(news3.content)

news4 = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=business&apikey=073c51d8af8f4ba88159626447b71cdb")
api4 = json.loads(news4.content)

news5 = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=technology&apikey=073c51d8af8f4ba88159626447b71cdb")
api5 = json.loads(news5.content)


def index(request):
    # fetch news 
    # render thtt news the home page templaet
    # india
    #print(api)
    #global api
    print(api1['articles'][0]['urlToImage'])
    context = {
    'img1' : api1['articles'][0]['urlToImage'],
    'img2' : api2['articles'][1]['urlToImage'],
    'img3' : api3['articles'][2]['urlToImage'],
    'img4' : api4['articles'][3]['urlToImage'],
    'img5' : api5['articles'][3]['urlToImage'],
    't1' : api1['articles'][0]['title'],
    't2' : api2['articles'][1]['title'],
    't3' : api3['articles'][2]['title'],
    't4' : api4['articles'][3]['title'],
    't5' : api5['articles'][3]['title'],


    'img1_1' : api1['articles'][0]['urlToImage'],
    'img1_2' : api1['articles'][1]['urlToImage'],
    'img1_3' : api1['articles'][2]['urlToImage'],
    'img1_4' : api1['articles'][3]['urlToImage'],

    't1_1' : api1['articles'][0]['title'],
    't1_2' : api1['articles'][1]['title'],
    't1_3' : api1['articles'][2]['title'],
    't1_4' : api1['articles'][3]['title'],

    'd1_1' : api1['articles'][0]['description'],
    'd1_2' : api1['articles'][1]['description'],
    'd1_3' : api1['articles'][2]['description'],
    'd1_4' : api1['articles'][3]['description'],


    'img2_1' : api2['articles'][0]['urlToImage'],
    'img2_2' : api2['articles'][1]['urlToImage'],
    'img2_3' : api2['articles'][2]['urlToImage'],
    'img2_4' : api2['articles'][3]['urlToImage'],

    't2_1' : api2['articles'][0]['title'],
    't2_2' : api2['articles'][1]['title'],
    't2_3' : api2['articles'][2]['title'],
    't2_4' : api2['articles'][3]['title'],

    'd2_1' : api2['articles'][0]['description'],
    'd2_2' : api2['articles'][1]['description'],
    'd2_3' : api2['articles'][2]['description'],
    'd2_4' : api2['articles'][3]['description'],


    'img3_1' : api3['articles'][0]['urlToImage'],
    'img3_2' : api3['articles'][1]['urlToImage'],
    'img3_3' : api3['articles'][2]['urlToImage'],
    'img3_4' : api3['articles'][3]['urlToImage'],

    't3_1' : api3['articles'][0]['title'],
    't3_2' : api3['articles'][1]['title'],
    't3_3' : api3['articles'][2]['title'],
    't3_4' : api3['articles'][3]['title'],

    'd3_1' : api3['articles'][0]['description'],
    'd3_2' : api3['articles'][1]['description'],
    'd3_3' : api3['articles'][2]['description'],
    'd3_4' : api3['articles'][3]['description'],


    'img4_1' : api4['articles'][0]['urlToImage'],
    'img4_2' : api4['articles'][1]['urlToImage'],
    'img4_3' : api4['articles'][2]['urlToImage'],
    'img4_4' : api4['articles'][3]['urlToImage'],

    't4_1' : api4['articles'][0]['title'],
    't4_2' : api4['articles'][1]['title'],
    't4_3' : api4['articles'][2]['title'],
    't4_4' : api4['articles'][3]['title'],

    'd4_1' : api4['articles'][0]['description'],
    'd4_2' : api4['articles'][1]['description'],
    'd4_3' : api4['articles'][2]['description'],
    'd4_4' : api4['articles'][3]['description'],


    'img5_1' : api5['articles'][0]['urlToImage'],
    'img5_2' : api5['articles'][1]['urlToImage'],
    'img5_3' : api5['articles'][2]['urlToImage'],
    'img5_4' : api5['articles'][3]['urlToImage'],

    't5_1' : api5['articles'][0]['title'],
    't5_2' : api5['articles'][1]['title'],
    't5_3' : api5['articles'][2]['title'],
    't5_4' : api5['articles'][3]['title'],

    'd5_1' : api5['articles'][0]['description'],
    'd5_2' : api5['articles'][1]['description'],
    'd5_3' : api5['articles'][2]['description'],
    'd5_4' : api5['articles'][3]['description']

    }
    return render(request,'kel.html',context)

def phrase(request):
    # fetch  sports news 
    # render thtt news the sports page templaet
    #news = requests.get("https://newsapi.org/v2/top-headlines?category=sports&country=in&apikey=073c51d8af8f4ba88159626447b71cdb")
    #api = json.loads(news.content)
    #print(gg)
    phrase1 = request.GET['phrase']
    phr = requests.get("https://newsapi.org/v2/top-headlines?q={}&apikey=073c51d8af8f4ba88159626447b71cdb".format(phrase1)) 
    phr = json.loads(phr.content)
    Len = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    content = {}
    i=0
    for i in Len :
    #    #title.append(api['articles'][i]['title'])
    #    #content.append(api['articles'][i]['content'])
    #    #print(title)
    #    content[phr['articles'][i]['title']]=phr['articles'][i]['content']
        content[phr['articles'][i]['title']]=phr['articles'][i]['content']
    context = {
        'cate': phrase1,   
        'img1' : phr['articles'][0]['urlToImage'],
        'img2' : phr['articles'][1]['urlToImage'],
        'img3' : phr['articles'][2]['urlToImage'],
        'img4' : phr['articles'][3]['urlToImage'],
        'img5' : phr['articles'][4]['urlToImage'],
        't1' : phr['articles'][0]['title'],
        't2' : phr['articles'][1]['title'],
        't3' : phr['articles'][2]['title'],
        't4' : phr['articles'][3]['title'],
        't5' : phr['articles'][4]['title'],
        'Len' : Len,
    
           'content' : content,
           }
    return render(request,'gel.html',context)



category=['National','Science','Sports','Business','Technology']
api_list=[api1,api2,api3,api4,api5]

def criteria(request,cate):
    # fetch  international news 
    # render thtt news the international page templaet

    api= api_list[cate]
    Len = len(api['articles'])
    Len = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    #title = []
    content={}
    i=0
    for i in Len :
        #title.append(api['articles'][i]['title'])
        #content.append(api['articles'][i]['content'])
        #print(title)
        content[api['articles'][i]['title']]=api['articles'][i]['content']
    
    context = {
    'cate': category[cate],   
    'img1' : api['articles'][0]['urlToImage'],
    'img2' : api['articles'][1]['urlToImage'],
    'img3' : api['articles'][2]['urlToImage'],
    'img4' : api['articles'][3]['urlToImage'],
    'img5' : api['articles'][4]['urlToImage'],
    't1' : api['articles'][0]['title'],
    't2' : api['articles'][1]['title'],
    't3' : api['articles'][2]['title'],
    't4' : api['articles'][3]['title'],
    't5' : api['articles'][4]['title'],
    'Len' : Len,
    
    'content' : content,
    }
    return render(request,'gel.html',context)

def miscel1(request):
    return render(request,'pel.html')

def miscel(request):
    #print('hello')
    a = request.GET['country']
    b = request.GET['keyword']
    if (request.GET['category']!= ''):
        c = request.GET['category']  

    country = {
        'Australia':'au',
        'Argentina':'ar',
        'Austria':'at',
        'Belgium':'be',
        'Brazil':'br',
        'Bulgaria':'bg',
        'Canada':'ca',
        'China':'cn',
        'Colombia':'co',
        'Cuba':'cu',
        'Czechia':'cz',
        'Germany':'de',
        'Egypt':'eg' ,
        'France':'fr',
        'England':'gb',
        'Greece':'gr',
        'HongKong':'hk',
        'Hungary':'hu',
        'Indonesia':'id',
        'Ireland':'ie',
        'Israel':'il',
        'India':'in',
        'Italy':'it',
        'Japan':'jp',
        'Korea':'kr',
        'Lithuania':'lt',
        'Latvia':'lv',
        'Morocco':'ma',
        'Mexico':'mx',
        'Malaysia':'my',
        'Nigeria':'ng',
        'Nicaragua':'nl',
        'Norway':'no',
        'New Zealand':'nz',
        'Philippines':'ph',
        'Poland':'pl',
        'Portugal':'pt',
        'Romania':'ro',
        'Serbia':'rs',
        'Russia':'ru',
        'Saudi Arabia':'sa',
        'Sweden':'se',
        'Singapore':'sg',
        'Slovenia':'si',
        'Slovakia':'sk',
        'Thailand':'th',
        'Turkey':'tr',
        'Taiwan':'tw',
        'Ukraine':'ua',
        'USA':'us',
        'Venezuela':'ve',
        'South Africa':'za',
    }
    e= country[a]
    if (request.GET['category']!= ''):
            news9 = requests.get("https://newsapi.org/v2/top-headlines?q={}&country={}&category={}&apikey=073c51d8af8f4ba88159626447b71cdb".format(b,e,c))
            api9 = json.loads(news9.content)
    else:
            news9 = requests.get("https://newsapi.org/v2/top-headlines?q={}&country={}&apikey=073c51d8af8f4ba88159626447b71cdb".format(b,e))
            api9 = json.loads(news9.content)


    d = a
    Len = api9['totalResults']

    content={}
    print(api9)
    for i in range(0,Len) :
        #title.append(api['articles'][i]['title'])
        #content.append(api['articles'][i]['content'])
        #print(title)
        content[api9['articles'][i]['title']]=api9['articles'][i]['content']

    context = {
    'cate': a,   
    'img1' : api9['articles'][0]['urlToImage'],
    'img2' : api9['articles'][1]['urlToImage'],
    'img3' : api9['articles'][2]['urlToImage'],
    'img4' : api9['articles'][3]['urlToImage'],
    'img5' : api9['articles'][4]['urlToImage'],
    't1' : api9['articles'][0]['title'],
    't2' : api9['articles'][1]['title'],
    't3' : api9['articles'][2]['title'],
    't4' : api9['articles'][3]['title'],
    't5' : api9['articles'][4]['title'],
    'Len':Len,
    'content': content  }
    return render(request,'gel.html',context)

def hear(request):
    engine.say('hello n')
    engine.startLoop()
    engine.stop()
    return render(request,'tel.html')











