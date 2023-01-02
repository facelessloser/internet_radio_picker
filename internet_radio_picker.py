import random, os, datetime 
from time import strftime

class Thelist(object):

    def station_one(self):
        os.system("mplayer http://uk1-pn.webcast-server.net:8698/")

    def station_two(self):
#        os.system("mplayer http://stream.drumandbass.fm:9002")
        os.system("mplayer http://trace.dnbradio.com:8000/dnbradio_main.mp3")


    def station_three(self):
        os.system("mplayer http://stream2.jungletrain.net:8000/")

    def station_four(self):
        os.system("mplayer http://tachyon.shoutca.st:8586/stream/;")

    def station_five(self):
        os.system("mplayer http://edge-bauerall-01-gos2.sharp-stream.com/kisstory.mp3?aw_0_1st.sk")
        
if __name__ == '__main__':
    start = Thelist()
print ('''
d d s  b sss sssss d sss   d ss.  d s  b d sss   sss sssss
S S  S S     S     S       S    b S  S S S           S
S S   SS     S     S       S    P S   SS S           S
S S    S     S     S sSSs  S sS'  S    S S sSSs      S
S S    S     S     S       S   S  S    S S           S
S S    S     S     S       S    S S    S S           S
P P    P     P     P sSSss P    P P    P P sSSss     P

d ss.  d s.   d ss    d   sSSSs
S    b S  ~O  S   ~o  S  S     S
S    P S   `b S     b S S       S
S sS'  S sSSO S     S S S       S
S   S  S    O S     P S S       S
S    S S    O S    S  S  S     S
P    P P    P P ss"   P   "sss"
 ''')
asking = input("""Enter the number of what you want to do:\n'1'> Kool london\n'2'> 24/7 drum and bass\n'3'> Jungletrain\n'4'> Origin uk\n'5'> Kisstory\n'6'> Exit\n> """)
if asking == "1":
    start.station_one()
elif asking == "2":
    start.station_two()
elif asking == "3":
    start.station_three()
elif asking == "4":
    start.station_four()
elif asking == "5":
    start.station_five()
elif asking == "6":
    exit()
else:
    print ("Something went wrong")
