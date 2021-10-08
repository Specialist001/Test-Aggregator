from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup as BSoup
from upl.models import Articles


def scrape(request):
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://upl.uz"

    content = session.get(url, verify=False).content
    soup = BSoup(content, "html.parser")
    articles = soup.find_all('div', {"class": "short-story"})

    for article in articles:
        image = article.find('div', {"class": "sh-img"}).find('img')['data-src']
        title = article.find('h2', {"class": "sh-tit"}).find('a').contents[0]
        link = article.find('h2', {"class": "sh-tit"}).find('a')['href']

        new_article = Articles()
        new_article.title = title
        new_article.image = url + image
        new_article.url = link
        new_article.save()

    return redirect("/upl")


def articles_list(request):
    articles = Articles.objects.all()[::-1]
    context = {
        'object_list': articles
    }

    return render(request, "upl/home.html", context)
