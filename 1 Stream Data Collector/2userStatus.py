from tweepy import OAuthHandler
from tweepy import Stream
import time, tweepy, sys, json,time
reload(sys)
sys.setdefaultencoding('utf8')
## authentication
# Rate Time : https://dev.twitter.com/rest/public/rate-limits
def main():
    access_token = []
    access_token_secret = []
    consumer_key = []
    consumer_secret = []
    key=0
    start_time = time.time()
    ## Original Key
    access_token.append('340666906-vR1jFZTZvtifH0eokIQ5s3Bc8XY1yoS99rLls0dF')
    access_token_secret.append('pQCc7Kob5DGIwk8VgRsen2lpmjZEFPcsXPoICoiZTSWXk')
    consumer_key.append('Tn9qySwDkCPTkLn75WW1wUABS')
    consumer_secret.append('DiuiK9qflmbVsIq3mfbFwDRgBQ776bTCDTLhWF4UlbPBFwCYsb')
    ## Backup Key 1
    access_token.append('340666906-8SlTI2G8aIi734bqvZTOVIq7L8kW8ZxPnSzuAA24')
    access_token_secret.append('Z5CFspMNb4Q2h5V3ij6V65aqM2MhAgRTWJcb8GG9DarMR')
    consumer_key.append('5cbqExNTsq7inIyMxj6eQybSK')
    consumer_secret.append('N3UE3pj6IMZeBqVLo0pLUrXPxLwJVgUs7gReqEXlx0ucDj0f58')
    ## Backup Key 2
    access_token.append('340666906-1l5SFVfxl53BnPgRYaRk6jkcHy9JMp82WKJXTvEv')
    access_token_secret.append('8K1r7lfVGWPR5LGVeYRWNk4R2aY565pNguVAQXUBuMUua')
    consumer_key.append('VORK8Y38RZ6TXzJvUJxcBq14Q')
    consumer_secret.append('VJNH1rXOtYBANOvJcHnf41q7UcGnDzojnOQGX19dqiuLyD4Aam')
    ## Backup Key 3
    access_token.append('340666906-BS2By3pR1Ibwlrn2InoQMpFN1ZCEWiAHoQn9jKnP')
    access_token_secret.append('IXzPaBhF5khI2On35UK758zKXECg5WdK8QyhuHwZfdrA4')
    consumer_key.append('vzbjLseblcD5sRmiloyVFdEjG')
    consumer_secret.append('ubbkGnvqglz0vApGqVU0SLGSV0pOftY46yG3kcGlvko7gcKIBL')
    ## Claudia Keys
    ## Backup Key 4
    access_token.append('270650088-90xnoKEziNziFB09F8liXfqUhHibzUUACnkUn8WJ')
    access_token_secret.append('Wc8uzahsXxYy97SQsAbvYMOmY2HTQCnm5GLs95MEBwuKG')
    consumer_key.append('EToBVoMBWFhqaewlfr5FhbGvD')
    consumer_secret.append('XeykrcEqsYcmEMw5CxCULX7dUe3hR4lz1EwzjjJbfzXVjbVqxR')
    ## Backup Key 5
    access_token.append('270650088-VtGnIkfD9VgVEaTrgvDDdlIB9GDjC5Pbh4NdHzUm')
    access_token_secret.append('jMLUvdWDlGwvlC32Az5W57jt0iFimZZrevTbHIixTboPh')
    consumer_key.append('cYDNaKhXZ6T4ydMa9TuzvLDtc')
    consumer_secret.append('Fv9QdpUpFrGfQQMXRnhvqwmxi8fLgfoxYidjlnO9nQ5GERvjWA')
    ## Backup Key 6
    access_token.append('270650088-EsAH0J5qdVmllIuxtIIYuN4AJrabKVjG7lnI4nzp')
    access_token_secret.append('40tZdloMs0vs6xAEimhkz48DXyZdGAKytInayaxwPfGCi')
    consumer_key.append('XrdojfBkvnYpBGyYWpDg3shRr')
    consumer_secret.append('9iKTCtb8XPFDQXQCPQw0qOZjMQgVprF1OuTJXFzeIW5uenxeDZ')
    ## Mauricio Keys
    ## Backup Key 7
    access_token.append('4893983668-HOlloxR5scyVcTLv7u3g9BvT19KP2DuN7dvM2O0')
    access_token_secret.append('g48CjCYZReiePCVL9N0anYlfEWT5WylvIbaGAgySorc6N')
    consumer_key.append('wMh4cTJ6GxjKH8sRSNmh7KfRm')
    consumer_secret.append('vn0wBhDG8nG245R2nRoHkc2Waqx76ml2hT0UbBWt6qER1YjGYt')
    ## Backup Key 8
    access_token.append('4893983668-eCY16Cowvbq496wSlnktquqAc1RjRaAocUVpVVX')
    access_token_secret.append('Xm4u20abddXsPZ4ZNWotQXMduqDyJPPyYTKnc4DN7FGZO')
    consumer_key.append('aNHI8xZKFmMhU8ImZeLIcZar4')
    consumer_secret.append('v6APOOVGfx7g15tjsb0feWe5rqKaukZ0auNW76otJQfUpEW7EV')
    ## Backup Key 9
    access_token.append('4893983668-SRdQFXqJOSozt6La2nfCseLyyZVxo9iMR9HG2S4')
    access_token_secret.append('DE2ckolUMPnXm1wKaa3dZ8RYKxnYmDaOqMr4hWgspxEc2')
    consumer_key.append('Zr1YTJrFDUMEs4UB0bdqlPdh0')
    consumer_secret.append('QatCrEzwWKzdv7s5f79nKmuEVbx7PGqNWO7b3qHtiO9ifLFwMk')
    ## Rueben KEYS
    ## Backup Key 10
    access_token.append('610967205-DvkMOjFEFlODH8fq9vsO8mEYF8NlnnK1MFXswtZY')
    access_token_secret.append('jzRTChJ4kWIErhqLAZYcdaHCvBdiEetPeWXXzfqH7i0C6')
    consumer_key.append('1vO6YD9eO6UlWe2X7t11a5NWZ')
    consumer_secret.append('bQ8xZkPI32c1ugqf5XQHCgqAwhCz66KReNREpj5BUSlP8uvmVn')
    ## Backup Key 11
    access_token.append('610967205-gVOwiGifckAMwmBfTkaZssjxMLnAc8aYzFU7cM7W')
    access_token_secret.append('Rt0UcDZPBXshvOdg0QTrzzkZ6diSCLkqb0nKd9GlHFbD0')
    consumer_key.append('xjZNghnm3gpoBlRetJtzI7xcU')
    consumer_secret.append('8t6eqZsznrhcWF34IN8rhSVY3UGoYWghgZImX5MRZusRDz9Cde')
    ## Backup Key 12
    access_token.append('610967205-6i2e3KuyytDhgvoRJa1tmDs0wiax1lqeUdx425o7')
    access_token_secret.append('OD8jV3xcpFk1xgmeqQK0uaP7JsA4m2hp1Po5T10vOoas4')
    consumer_key.append('zLLoDiPuggePKFYi7m6UFy8UM')
    consumer_secret.append('7vP7m7ZbOGCooLIrdFV9YvyuGumBvOerEQ3rZhFF4bs4jTs52I')
    ## Diana KEYS
    ## Backup Key 13
    access_token.append('3393835121-5bsJPCvQltXKDsktSCz4OczAtZgjqbMJjS5vJKd')
    access_token_secret.append('PoEzXd5VcsceBAh4cWjHexCboEKByQD4F2jcrZn27TlTC')
    consumer_key.append('1q8ebidR8tvhcNbkVxfwXu6ny')
    consumer_secret.append('fKtefSXdCnkVw2niGLNOyBV1hftTmFhfNaHTviQMnVIBoip3HH')
    ## Backup Key 14
    access_token.append('3393835121-0ZLNAzRxcjrIvGneahiZipPetscKKm5p4mw2hiH')
    access_token_secret.append('36rZkfe0UUYhs58oMoUYhbrqSPuvlyiYpx7RCYKe8L7BS')
    consumer_key.append('7oGTUv7YPF9fcBTvPhacspH9d')
    consumer_secret.append('ONdye4IOTcYfpdgIM8WOuQokUkRHmP33Cjf1KUjRT88x04fI6W')
    ## Backup Key 15
    access_token.append('3393835121-Gyzwk8JepPfO4mFb3WfscB0nFvzNh30WY9EuUAd')
    access_token_secret.append('BW2Dn41cDpmAjMl6UvXa9bhcawF8IrNqJ96qSuAYGKx8d')
    consumer_key.append('IIFqkHrnqOZkvpWwpkJsOHqQU')
    consumer_secret.append('w0ssZJ98UPg1QCsSmlWpKRiKfFTzeMoiwpxmedHEDgJ54PXGbc')
    ## Otro KEYS
    ## Backup Key 16
    access_token.append('2364261902-CA01YAyNqrxn8bg1mbzCSnmfeW3VkaUcddW6Mzt')
    access_token_secret.append('dWudJI1jZy6fe9OjEKBD4UUZStu5qgtgT7DUFQH7OPyjb')
    consumer_key.append('CBlaOful60gFYlIDopDXP7BHL')
    consumer_secret.append('677l3Ff7gSWRJelSB7dTcQsG5CxByQFwXWB4LrAcSVg8Yn7dvG')
    ## Backup Key 17
    access_token.append('2364261902-iZLw2U4LwZnmxSn32pZOpeFSd1IGaw7FSHw58j4')
    access_token_secret.append('jut9Ds32UlDv1Hy4uAbHm7ZchxYrIbcCAzEeKCyl2CdHJ')
    consumer_key.append('QaNkLWTAoq6UUNEywTcDLSbKb')
    consumer_secret.append('MXL71WPA3Nedd51nwzZ3wcbKawbiq11WLkm0BCsyh7IPv8SV6h')
    ## Backup Key 18
    access_token.append('2364261902-0irIfYaoyqxq3udZIfhXdKLv35cBHB5DCGp6CXt')
    access_token_secret.append('1sS4QLwSKNpSIBOcctqRnMDQfaUJRwWWePIuww1nW0boi')
    consumer_key.append('hDrbYYZ0SwO9Cozea41DBtTCo')
    consumer_secret.append('yI7MJ96dR64g2t9UMJ2xV4T9dlfTFwnh3w2fiqWwjmQDNah86R')



    limit=len(access_token);

    auth = OAuthHandler(consumer_key[key], consumer_secret[key])
    auth.set_access_token(access_token[key], access_token_secret[key])
    api = tweepy.API(auth,wait_on_rate_limit=False)

    inp=open("../Record/Finals/result-filter.data",'r')
    #inp=open("Record/mini-sampleResult.json",'r')
    prefix="X2Search.data";
    out= open(prefix,'ab');
    tweetCount=99999999999999999999999999999999999999999999
    tweetCount=0
    errors=99999999999999999999999999999999999999999999
    errors=0
    cambios=0
    #roer=open("userErrors",'ab')
    for line in inp:
        tweet = line.rstrip('\n')
        if tweet!="":
            tweetCount+=1
            tweetJson   = json.loads(tweet)
            tws=0;
            try:
                userName    =tweetJson['user']['screen_name']
                status_list = api.user_timeline(screen_name=userName)
                for status in status_list:
                #for status in tweepy.Cursor(api.user_timeline, id="twitter").items(200): #status_list:
                    json_str = json.dumps(status._json)
                    if 'text' in json_str:
                        out.write(json_str.encode('utf-8')+"\n")
                        tws+=1
                    #out.write("a\n")
                print(str(tweetCount)+")  "+userName+" - "+str(tws))
                #out.write("]")
            except tweepy.RateLimitError as a:
                key+=1
                cambios+=1
                print("*)Haciendo cambio de llaves...............  cambio numero: "+ str(cambios)+ "   Llave actual: "+str(key))
                if key>=limit:
                    key=0

                    if (time.time() - start_time) < 905:
                        print("*)RateLimitError -- Esperado tiempo de ventana "+ str((900 - (time.time() - start_time))))
                        time.sleep(900 - (time.time() - start_time) +5 )
                    start_time=time.time()

                auth = OAuthHandler(consumer_key[key], consumer_secret[key])
                auth.set_access_token(access_token[key], access_token_secret[key])
                api = tweepy.API(auth,wait_on_rate_limit=False)

                try:
                    userName    =tweetJson['user']['screen_name']
                    status_list = api.user_timeline(screen_name=userName)
                    for status in status_list:
                    #for status in tweepy.Cursor(api.user_timeline, id="twitter").items(200): #status_list:
                        json_str = json.dumps(status._json)
                        if 'text' in json_str:
                            out.write(json_str.encode('utf-8')+"\n")
                        #tws+=1
                        #out.write("a\n")
                    print(str(tweetCount)+")  "+userName+" - "+str(tws))
                except:
                    print("Error no esperado ("+userName+")"  )
                #    roer.write(userName+ " ---- "+ str(b)+"\n")
                #    print("--------------Dormir por 5 segundos -----------------")
                    #time.sleep(5)
            except tweepy.TweepError as b:
                #errors+=1
                print(str(tweetCount)+")  "+userName+" ------------ Error! Cuenta privada? "+str(errors))
                #roer.write(userName+ " ---- "+ str(b)+"\n")
                #print("--------------Error -----------------")
                #time.sleep(5)
            except Exception as c:
                print(" ------------ ------------ Other type of error "+str(c))
                #roer.write(userName+ " ---- "+ str(c)+"\n")
                #print("--------------Error -----------------")
                #time.sleep(5)
    print("\n \n Errors = "+ str(errors)+"\n \n")
    #roer.close()
    inp.close()
    out.close()

if __name__ == '__main__':
    main()
