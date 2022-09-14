class Movie:
    def __init__ (self, title, genre, director, year):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
    def get_title (self):
        return self.title
    def get_genre (self):
        return self.genre
    def get_director (self):
        return self.director
    def get_year (self):
        return self.year

class StreamingService:
    def __init__ (self, name):
        self.name = name
        self.catalog = {}
    def get_name (self):
        return self.name
    def get_catalog (self):
        return self.catalog
    def add_movie (self, mov):
        self.catalog[mov.get_title ()] = mov
    def delete_movie(self, mtitle):
        del self.catalog [mtitle]

class StreamingGuide:
    def __init__ (self):
        self.sslist = []
    def add_streaming_service (self, ss):
        self.sslist.append (ss)
    def delete_streaming_service (self, ss):
        if ss in self.sslist:
            self.sslist.remove (ss)
    def where_to_watch_movie (self, mtitle):
        retlst = []
        for svc in self.sslist:
            if mtitle in svc.get_catalog():
                mov = svc.get_catalog()[mtitle]
                if retlst == []:
                    retlst = [mov.get_title () + " (" + str (mov.get_year ()) + ")"]
                retlst.append (svc.get_name ())
            else:
                return None
        return retlst

movie_1 = Movie('The Seventh Seal', 'comedy', 'Ingmar Bergman', 1957)
movie_2 = Movie('Home Alone', 'tragedy', 'Chris Columbus', 1990)
movie_3 = Movie('Little Women', 'action thriller', 'Greta Gerwig', 2019)
movie_4 = Movie('Galaxy Quest', 'historical documents', 'Dean Parisot', 1999)

stream_serv_1 = StreamingService('Netflick')
stream_serv_1.add_movie(movie_2)

stream_serv_2 = StreamingService('Hula')
stream_serv_2.add_movie(movie_1)
stream_serv_2.add_movie(movie_4)
stream_serv_2.delete_movie('The Seventh Seal')
stream_serv_2.add_movie(movie_2)

stream_serv_3 = StreamingService('Dizzy+')
stream_serv_3.add_movie(movie_4)
stream_serv_3.add_movie(movie_3)
stream_serv_3.add_movie(movie_1)

stream_guide = StreamingGuide()
stream_guide.add_streaming_service(stream_serv_1)
stream_guide.add_streaming_service(stream_serv_2)
stream_guide.add_streaming_service(stream_serv_3)
stream_guide.delete_streaming_service('Hula')
search_results = stream_guide.where_to_watch_movie('Little Women')

print(search_results)