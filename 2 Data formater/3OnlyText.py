from tweepy import OAuthHandler
from tweepy import Stream
import time, tweepy, sys, json,time

reload(sys)
sys.setdefaultencoding('utf8')

## authentication
# Rate Time : https://dev.twitter.com/rest/public/rate-limits
def main():

    #inp=open("../Record/Finals/result-filter.data",'r')
    inp=open("../Record/result-filter.data",'r')
    #inp=open("Record/mini-sampleResult.json",'r')
    #prefix="../Record/Finals/result-OnlyText "+time.strftime('%Y_%m_%d-%H:%M:%S')+".data";
    prefix="../Record/Finals/X2Search-OnlyText "+time.strftime('%Y_%m_%d-%H:%M:%S')+".data";
    #prefix="Record/result-OnlyText "+time.strftime('%Y_%m_%d-%H:%M:%S')+".json";
    out= open(prefix,'ab');
    obs= open("Observer.data",'ab');
    cou=999999999999999999999999999
    cou=0
    capture=999999999999999999999999999
    capture=0
    dana=999999999999999999999999999
    dana=0
    for line in inp:
        tweet = line.rstrip('\n')
        if tweet!="":
            try:
                tweetJson   = json.loads(tweet)
                if 'text' in tweetJson:
                    #print(tweetJson)
                    ##Limpiando el observador de ultimo error
                    #obs.seek(0)
                    #obs.truncate()
                    ## guardando el ultmimo tweet con error
                    #obs.write(str(tweetJson)+"\n")
                    #text =tweetJson['id_str']+ " " + tweetJson['text'].replace("\n"," ").encode('utf-8')
                    text =tweetJson['id_str']+ " " + tweetJson['text'].replace("\n"," ")
                    out.write(str(text)+"\n")
                    capture+=1
                else:
                    dana+=1

            except Exception, c:
                print("*) Other type of error "+str(c))
                cou+=1
    print("capturados : "+str(capture)+ "  ----- Danados : "+str(dana)+ " --- Errores: "+str(cou))
    inp.close()
    out.close()

if __name__ == '__main__':
    main()
