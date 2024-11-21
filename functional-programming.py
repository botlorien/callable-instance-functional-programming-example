from functools import reduce
from operator import mul, itemgetter, attrgetter, methodcaller
from collections import namedtuple

def factorial(n):
    return reduce(lambda a,b:a*b,range(1,n+1))


def factorial2(n):
    return reduce(mul,range(1,n+1))

if __name__=='__main__':
    # Fatorial sem recursão e com lambda
    print(factorial(5))

    # Fatorial sem recursão e sem lambda
    print(factorial2(5))

    # Usando outras funções de operator que evitam construções de funções desnecessarias
    metro_data = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]

    # Itemgetter
    for city in sorted(metro_data,key=itemgetter(1)):
        print(city)

    cc_name =  itemgetter(1,0)
    print(cc_name)
    for city in metro_data:
        print(cc_name(city))

    # Attrgetter
    LatLon = namedtuple('LatLon','lat lon')
    Metropolis = namedtuple('Metropolis','name cc pop coord')

    metro_areas = [Metropolis(name,cc,pop,LatLon(lat,lon)) for name, cc, pop, (lat,lon) in metro_data]
    print(metro_areas[0])
    print(metro_areas[0].coord.lat)
    name_lat = attrgetter('name','coord.lat')
    for city in sorted(metro_areas,key=attrgetter('coord.lat')):
        print(name_lat(city))

    # Methodcaller
    s = 'The time has come'
    upcase = methodcaller('upper')
    print(upcase(s))
    hyphenate = methodcaller('replace',' ','-')
    print(hyphenate(s))
