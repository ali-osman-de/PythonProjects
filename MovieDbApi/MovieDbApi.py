

import requests


class movieDb:

    def __init__(self):
        self.api_url = 'https://api.themoviedb.org/3/search/keyword?api_key={0}&query={1}&page={2}'
        self.api_key = '8a167580a0125a03517fab1c7fd8b442'
        self.popular_api_url = 'https://api.themoviedb.org/3/trending/movie/{0}?api_key={1}'
        self.upcoming_api_url = 'https://api.themoviedb.org/3/movie/upcoming?api_key={0}&language={1}&page={2}'
    
    def searchKeyValue(self, valueKey, pageNumber):
        response = requests.get(self.api_url.format(self.api_key, valueKey,pageNumber))
        return response.json()

    def findMostPopularMovie(self,which):
        response = requests.get(self.popular_api_url.format(which,self.api_key))
        return response.json()

    def upComingFilm(self,language,pageNumber):
        response = requests.get(self.upcoming_api_url.format(self.api_key,language,pageNumber))
        return response.json()



movie = movieDb()


while True:

    choose = input("""
                    1- Searh Film
                    2- Most Popular Film List
                    3- Upcoming Films
                    4- Exit
                    
                    Your Choose: """)
    
    if choose == '4':
        break
    
    else:

        if choose == '1':
            pageNumber = input('Arama yapmak istediğiniz sayfa numarasını giriniz: ')
            valueKey = input('Aratmak istediğiniz harfi giriniz: ')
            result = movie.searchKeyValue(valueKey,pageNumber)
            for i in result['results']:
                for i2 in i:
                    filmnames = i['name']
                    filmid = i['id']
                print("Film Names: {0} -- {1}".format(filmnames,filmid))

        elif choose == '2':
            choose2 = input("""
                            1- Günlük Trend
                            2- Haftalık Trend

                            Your Choose: 
                            """)
            if choose2 == '1':
                which = 'day'
                result = movie.findMostPopularMovie(which)
                for i in result['results']:
                    filmnames = i['title']
                    popularity = i['popularity']
                print("Film Names: {0}\nPopularity: {1}".format(filmnames,popularity))
            
            elif choose2 == '2':
                which = 'week'
                result = movie.findMostPopularMovie(which)
                for i in result['results']:
                    filmnames = i['title']
                    popularity = i['popularity']
                print("Film Names: {0}\nPopularity: {1}".format(filmnames,popularity))
        elif choose == '3':
            pageNumber = input('Arama yapmak istediğiniz sayfa numarasını giriniz: ')
            lang = input('Hangi dilde arama yapacaksınız(en): ')
            country = input('Hangi bölge için arama yapacaksınız(US): ')
            language = lang + "-" + country
            result = movie.upComingFilm(language, pageNumber)
            for i in result['results']:
                for i2 in i:
                    filmnames = i['original_title']
                    filmid = i['original_language']
                    filmrelease = i['release_date']
                print(f"Film Names: {filmnames}\nFilm Language: {filmid}\nFilm Releas Date: {filmrelease}")
                print("----------------------------------------")
        else:
            print("Something went wrong!")