##### PLACE HOLDER
"""
name = input("who are you? ")
print("hello %s" % (name))
"""



###### FEHLERBEHANDLUNG
"""
#i = input ("gib eine ganze Zahl ein: ")
#print(int(i))        #Fehler wenn i!=integer

#Lösung mit 'try', 'except' und 'finally'
#i = input("Gib eine ganze Zahl ein: ") 
#try:
#    x = int(i)
#except ValueError:     #optional
#    print("Es ist keine ganze Zahl")
##except OtherError...
#else: 
#   print(x)
#finally:
#    print("Programm endet hier")#
"""



###LIST######
"""
bikes=[]
bikes.append('trek')
bikes.append('fitness')
bikes.append('giant')
bikes.append('city')
print(bikes[:])
bikes.sort(reverse=True)
print(bikes)
"""

"""
squares = []
for x in range(1, 11): 
    squares.append(x**2)
    #print(squares[x-1])

print(9 in squares)    #is 9 in squares? ---> True

ksquares = squares[0:3]     #slice a List
lsquares = squares          #copy a list
print(ksquares)
print(lsquares)
squares[1]='ahaha'          #change a element
#del squares[:]             #delete all elements
#del squares                #del the list
squares.remove('ahaha')     # == del square[1]
print(squares.pop())        #take the (last) element off
print(squares)

print(str(len(squares)))    #length of list in str



x = list(range(1,21))
print(x)



names = ['chan', 'vai', 'lon', 'cac', 'ban', 'a']
upper_names=[]

for name in names:
    upper_names.append(name.upper())
    print(name.upper(), end = ' ')

print(names) 
print(upper_names)
"""




#######TULPE#########
"""
Family = ('dad', 'mom', 'son')
print(Family[-1])

name = input("What's your name? ") 
print("Hello, " + name + "!")
"""


############ DICTIONARY ######
"""
fav_numbers = {'eric': 17, 'ever': 4} 
for name, number in fav_numbers.items(): 
    print(name + ' loves ' + str(number))

for name in fav_numbers.keys():
   print('name: ' + name)

print ('alo' + str(3))

for number in fav_numbers.values():
   print(str(number))
"""


"""
Namelist = []
Schuhgröße = {'Kinh':40.5, 'Thao':37.5, 'Chut':36}
for Name, Größe in Schuhgröße.items():
    print (Name + ' trägt ' + str(Größe))
    Namelist.append(Name)
print(Namelist)
# add a key-value pair
Schuhgröße['xanh'] = 36
print(Schuhgröße.popitem())
print(Schuhgröße)
"""


"""
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
"""

########### WHILE LOOP ########


"""
string = 'a s d f g h'
y=0
print(len('asdasdasd'))
print(string[3])
for x in string:
    if x == ' ':
        y = y + 1
print(y)

frage = ''
while frage != 'y':
frage = input('quit (y/n) ')"""

"""
prompt = "\nWhat cities have you visited?" 
prompt += "\nEnter 'quit' when you're done. " 
while True: 
    city = input(prompt) 
    if city == 'quit': 
        break 
    else: print("I've been to " + city + "!")
"""



######## FUNCTION ########
"""
def sqrt(x):
    x = x * x
    print(x)

sqrt(234)


def fEssen(Essen = 'rice'):

print('your meal is ' + str(Essen))

fEssen('sdfsf')
"""

##### CLASS ############ 

"""
class Mitarbeiter:

    def __init__(self, Vor, Lohn, Nach):
        self.vor = Vor
        self.nach = Nach
        self.lohn = Lohn
    
    def Name(self):
        print('{} {}'.format(self.vor, self.nach))

    def Email(self):
        print(self.vor + '.' + self.nach + '@kls.de')
    

#mit1 = Mitarbeiter('Kinh', 'Nguyen', 10)

#mit1.Name()
#mit1.Email()

class Praktikant(Mitarbeiter):
    def __init__(self, Vor, Lohn, Nach, geb, gender):
        super().__init__(Vor, Lohn, Nach)
        self.geb = geb
        self.gender = gender
        print('aaaaaa')
        
    def Geburtstag(self):
        print(self.geb)
        print(self.lohn)

prkt1 = Praktikant('Thao', 35, 'mai', 1994, 'female')
prkt1.Email()
prkt1.Geburtstag()
# prtk1.__init__()   ### __init__() ist nicht dafür gedacht

class Zeitarbeiter(Mitarbeiter):
    pass

#zab1 = Zeitarbeiter('K', 13, 'Ng')
#zab1.Name()
#zab1.Email()
#print(zab1.vor)


users = []
new_user = {'last':'fermi', 'first':'enrico', 'username':'efermi'}
users.append(new_user)
print(users)
users.append('das was')
print(users)

for info in users:
    for f,l in info.items():
        print(f,l, '\n')
"""

"""
fav_languages = {}                          # Store each person's languages, keeping # track of who respoded first.
fav_languages['jen'] = ['python', 'ruby'] 
fav_languages['sarah'] = ['c'] 
fav_languages['edward'] = ['ruby', 'go'] 
fav_languages['phil'] = ['python', 'haskell'] 
# Display the results, in the same order they # were entered. 
for name, langs in fav_languages.items():
     print(name + ":") 
     for lang in langs: 
         print("- " + lang)

"""


######## matplotlib / plot  #########



#Parabol#
"""

import matplotlib.pyplot as plt
x_values = []
y_values = []
for x in range(-50, 51):
    x_values.append(x)
    y_values.append(x*x)


#faster alternative
"""
"""
import matplotlib.pyplot as plt


x_values = list(range(-50, 51))
y_values = [x**2 for x in x_values]
"""
"""
plt.scatter(x_values, y_values, s=2)    #Punkte mit Size = 2
plt.plot(x_values, y_values)            #Kurve        
plt.show()                              # anzeigen lassen
"""

###Label / Titel 7 scaling axes
'''
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

red_patch = mpatches.Patch(color='yellow', label='The red data')
plt.legend(handles=[red_patch])

plt.show()
'''
"""

import matplotlib.pyplot as plt
x_values =  list(range(1000))
squares = [x**2 for x in x_values]

plt.scatter(x_values, squares, s=5)
plt.title('Parabol', fontsize =20)
plt.xlabel('Value', fontsize=16)
plt.ylabel('Square of Value', fontsize=16)
plt.tick_params(axis='x', direction='out', length=6, width=2, colors='r', grid_color='r', grid_alpha=0.5)
#This will make all major ticks of x-axle be red, pointing out of the box, and with dimensions 6 points by 2 points. Tick labels will also be red. Gridlines will be red and translucent.
plt.axis([0,1100, 0, 1100000])

plt.show()
"""

"""
import matplotlib.pyplot as plt

plt.ion()
#plt.axis([0,100, 0, 1000])
y=0
for i in range(100):
    x = range(i)
    y = range(i)
# plt.gca().cla() # optionally clear axes
    plt.plot(x, y)
    #plt.title(str(i))
    plt.draw()
    plt.pause(0.1)

plt.show(block=True)
"""

"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


def init():  # only required for blitting to give a clean slate.
    line.set_ydata([np.nan] * len(x))
    return line,


def animate(i):
    line.set_ydata(np.sin(x + i / 100))  # update the data.
    return line,


ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=2, blit=True, save_count=50)

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# from matplotlib.animation import FFMpegWriter
# writer = FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

plt.show()

"""
"""
import numpy as np
from numpy import sqrt
import matplotlib.pyplot as plt
import scipy as sp
import math

def sinyal(N,c,f,p):
    y=np.zeros(N)
    t=np.linspace(0,2*np.pi,N)
    Nf=len(c)
    for i in range(Nf):
        y+=c[i]*np.sin(f[i]*t)
    return y

 # Signal Generator
c=[2,5,10]
f=[50, 150, 300]
p=[0,0]
N=2000
x=np.linspace(0,2.0*math.pi,N)
y=sinyal(N,c,f,p)
plt.plot(x[:100],y[:100])
plt.show()
"""


"""
import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0,2*np.pi,0.05) #Datensaetze erzeugen
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.abs(np.sin(x))
y4 = np.abs(np.cos(x))

plt.plot(x, y1)
plt.plot(x, y2)

plt.title('Sinus, Cosinus')
plt.xlim([0,2*np.pi])
plt.show()
"""

######## plot kontinuierlicher Daten ###########
## https://riptutorial.com/de/matplotlib/example/26916/live-daten-von-pipe-mit-matplotlib-darstellen
##

"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
line, = ax.plot(np.random.rand(10))
ax.set_ylim(0, 1)


def update(data):
    line.set_ydata(data)
    return line,


def data_gen():
    while True:
        yield np.random.rand(10)

ani = animation.FuncAnimation(fig, update, data_gen, interval=100)
plt.show()
"""

