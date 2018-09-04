import json

import requests
from django.shortcuts import render
from newsapi import NewsApiClient


# Create your views here.
def headlineView(request):
    # Init
    newsapi = NewsApiClient(api_key='6e41c1d153b9441ea84f14aac376b486')

    # /v2/top-headlines
    # top_headlines = newsapi.get_top_headlines(q='bitcoin',
    #                                           sources='bbc-news,the-verge',
    #                                           category='business',
    #                                           language='en',
    #                                           country='us')
    # /v2/sources
    sources = newsapi.get_sources()

    # requesting data from api

    url = ('https://newsapi.org/v2/top-headlines?sources=bbc-news,cnn,google-news-in,the-hindu,the-times-of-india,the-telegraph&apiKey=6e41c1d153b9441ea84f14aac376b486')
    response = requests.get(url)
    s=json.loads(response.text)
    return render(request,'headline.html',{'newsheadline':s})



def sportsnews(request):
    url = ('https://newsapi.org/v2/top-headlines?sources=bbc-sport,talksport,fox-sports,football-italia,espn-cric-info&apiKey=6e41c1d153b9441ea84f14aac376b486')
    response = requests.get(url)
    sports_data = json.loads(response.text)

    return  render(request,'sports.html',{'sports':sports_data})


def entertainment(request):

    url = ('https://newsapi.org/v2/everything?sources=mtv-news,polygon,entertainment-weekly&apiKey=6e41c1d153b9441ea84f14aac376b486')
    response = requests.get(url)
    e_data = json.loads(response.text)

    return  render(request,'entertainment.html',{'entertainment':e_data})

def everything(request):

    url = ('https://newsapi.org/v2/everything?sources=mashable,bbc-news,cnn,news24,the-hindu,the-times-of-india,the-telegraph,bbc-sport,talksport,mtv-news,entertainment-weekly,fox-sports,football-italia,espn-cric-info&apiKey=6e41c1d153b9441ea84f14aac376b486')
    response = requests.get(url)
    everything_data = json.loads(response.text)

    return  render(request,'everything.html',{'everything':everything_data})

def technology(request):

    url = ('https://newsapi.org/v2/everything?sources=hacker-news,t3n,techcrunch,techradar&apiKey=6e41c1d153b9441ea84f14aac376b486')
    response = requests.get(url)
    tech_data = json.loads(response.text)

    return  render(request,'technology.html',{'tech':tech_data})


# def pagenotfound(request):
#     return render(request,'404.html')
