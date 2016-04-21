from slistener import SListener
#from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time, tweepy, sys
import os
reload(sys)
sys.setdefaultencoding('utf8')
## authentication
access_token='340666906-vR1jFZTZvtifH0eokIQ5s3Bc8XY1yoS99rLls0dF'
access_token_secret='pQCc7Kob5DGIwk8VgRsen2lpmjZEFPcsXPoICoiZTSWXk'
consumer_key='Tn9qySwDkCPTkLn75WW1wUABS'
consumer_secret='DiuiK9qflmbVsIq3mfbFwDRgBQ776bTCDTLhWF4UlbPBFwCYsb'
## Backup Key 1

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api      = tweepy.API(auth)

def main():
    prefix='X1Stream'
    track =[]
    """
    Obteniendo todas las palabras que se encuentras en el
    archivo diccionario guardandolas en la variable "track", se omiten
    lineas en blanco

    try:
        print "Tamano Inicial del archivo existente: " + str((os.path.getsize(prefix)/1024/1024)) + " MB"
    except:
        print "Creando archivo ..."
    """

    with open("diccionary.txt") as f:
        for line_terminated in f:
            line = line_terminated.rstrip('\n')
            if line!="" and not (line in track):
                track.append(line);

    print "Se agragaron  "+ str(len(track))+ " palabras DESDE el diccionario"
    while True:
    #    f=open('output.txt', 'w')
    #   f.write("\n".join(track))
        #track = ['obama', 'romney']
        listen = SListener(api, prefix)
        stream = tweepy.Stream(auth, listen)

        print "Streaming started..."
        try:
            #stream.filter(languages=['en'],track = track)
            stream.filter(track = track)
            #    print "{ ok el stream es el del problema}"
        except:
            print time.strftime('%H:%M:%S') + " error!  --- Intentado reconectar en 3s "
            #print "tamano del archivos : " + str((os.path.getsize(prefix)/1024/1024)) + " MB"
            #    time.sleep(3)
                #stream = tweepy.Stream(auth, listen)
                #stream.disconnect()

if __name__ == '__main__':
    main()
