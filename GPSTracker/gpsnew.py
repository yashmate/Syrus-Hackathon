import pandas as pd
from gmplot import gmplot
df=pd.read_csv('route.csv')
gmap=gmplot.GoogleMapPlotter(19,72,17)
gmap.coloricon="http://www.googlemapsmarkers.com/v1/%s/"
lat=df['LATITUDE'].values.tolist()
long=df['LONGITUDE'].values.tolist()
print(lat)
print(long)
for i in range(1,len(lat)-1):
    gmap.marker(lat[i],long[i],'yellow')
gmap.marker(lat[0],long[0],'red')
gmap.marker(lat[-1],long[-1],'blue')
gmap.draw('mymap.html')
from bs4 import BeautifulSoup

def insertapikey(fname, apikey):
    """put the google api key in a html file"""
    def putkey(htmltxt, apikey, apistring=None):
        """put the apikey in the htmltxt and return soup"""
        if not apistring:
            apistring = "https://maps.googleapis.com/maps/api/js?key=%s&callback=initMap"
        soup = BeautifulSoup(htmltxt, 'html.parser')
        body = soup.body
        src = apistring % (apikey, )
        tscript = soup.new_tag("script", src=src, async="defer")
        body.insert(-1, tscript)
        return soup
    htmltxt = open(fname, 'r').read()
    soup = putkey(htmltxt, apikey)
    newtxt = soup.prettify()
    open(fname, 'w').write(newtxt)

insertapikey("mymap.html", 'AIzaSyDLVzEeQJL8auhUl3yG5QnHyz30wMjYz6E')
