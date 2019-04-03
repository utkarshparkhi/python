import urllib.request
from bs4 import BeautifulSoup
import pythonassignment
class person:
    names = {}
    
    def __init__(self,name,**kwargs):
        if type(name)== type(''):
            if (name not in person.names.keys()):
                self.name=name
                person.names[name] = self
            else:
                raise Exception('name already exist')
        else:
            raise Exception('name must be a string')
        if 'work' in kwargs.keys():
            if type(kwargs['work'])==type([]):
                self.work = kwargs['work']
            else:
                raise Exception('work must be a list')
        if 'city' in kwargs.keys():
            if type(kwargs['city'])==type(''):
                self.city=kwargs['city']
            else:
                raise Exception('city must be a string')
        else:
            self.city='Roorkee'
    def show(self):
        print('My name is {} and my current city is {}'.format(self.name,self.city))
        return 'My name is {} and my current city is {}'.format(self.name,self.city)

def username_exist(func):
    def wrapper(*args):
        if pythonassignment.userexists(*args):
            return func(*args)
    return wrapper

@username_exist
def scrape(username):
    if username in person.names.keys():
        return person.names[username].show()
    else:

        fburl = 'https://en-gb.facebook.com/{}'.format(username)
        page = urllib.request.urlopen(fburl)
        soup = BeautifulSoup(page)
        per = person(username) 
        work = []
        
        i = soup.find("div",{'class':'_4qm1'})
        if i.find('span',{'class':'_h72 lfloat _ohe _50f7'}).text == 'Work':
            for k in i.find_all('div',{'class':'_6a _6b'}):
                if k.text !='':
                     a = ''
                     w = ''
                     if k.find('div',{'class':'_2lzr _50f5 _50f7'}) is not None:   
                        a = k.find('div',{'class':'_2lzr _50f5 _50f7'}).text
                     if k.find('div',{'class':'fsm fwn fcg'}) is not None:
                        w = k.find('div',{'class':'fsm fwn fcg'}).text
                        w = w.split(' · ')[0]
                     
                     wor = (' ').join((' ').join([str(a),str(w)]).split())
                 
                     work.append(wor)
                     if work != []:
                         per.work = work
        for i in soup.find_all("div",{'class':'_4qm1'}) :

             if(i.find('li',{'id':'current_city'})) is not None:
                    city=i.find('li',{'id':'current_city'}).a.text
                    per.city = city
        favourites = soup.find('div',{'class':'_5h60 allFavorites'})
        fav = {}
        if favourites is not None: 
            label = favourites.find_all('div',{'class':'labelContainer'})
        
            data = favourites.find_all('td',{'class':'data'})
            for i in range(len(label)):
                fav[label[i].text] = data[i].text
            print(fav)
            return fav
        else:
            return 'no favourites to show'
            print('no favourites to show')

        
    #scrape('swapnil.negi09')


