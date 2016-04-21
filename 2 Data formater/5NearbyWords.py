
from nltk.corpus import stopwords
import time, tweepy, sys, json,time

reload(sys)
sys.setdefaultencoding('utf8')

def main():
    STOP_TYPES=['DET','CNJ']
    """
    nltk.download('stopwords')
    stop=stopwords.words('english')
    """
    stop=stopwords.words('english')

     inp=open("../Record/Finals/X2Search-OnlyText.data",'r')
     inp2=open("../Record/Finals/X2Search-OnlyText.data",'r')

     array={}
     for line1 in inp:
         words1=line1.split(" ")
         words1=[word for word in words1 if word not in stop]
         #words1=''.join(words1)
         max0=0
         max1=0
         max2=0
         max3=0
         max4=0
         max5=0
         max6=0
         max7=0
         max8=0
         max9=0
         array['tweet']=line.split(" ")[0]
         for line2 in inp2:
            words2=line2.split(" ")
            words2=[word for word in words2 if word not in stop]
            #words2=''.join(words2)

            #Contando la cantidad de palabras que tiene en comun 2 tweets
            common = set(words1).intersection( set(words2) )
            c=len(common)
            if c>max0:
                max9=max8
                max8=max7
                max7=max6
                max6=max5
                max5=max4
                max4=max3
                max3=max2
                max2=max1
                max1=max0
                max0=c

            elif c>max1:
            elif c>max2:
            elif c>max3:
            elif c>max4:
            elif c>max5:
            elif c>max6:
            elif c>max7:
            elif c>max8:
            elif c>max9:

                pass

         tweet = line.rstrip('\n')
         if tweet!="":
             try:
                 print tweet
    #             break
    #         except:
    #             print "Error"
    #             break





    sentence="this is ais fothiso bar sentence".split(" ")

    filtered= [word for word in sentence if word not in stop]

    print sentence
    print ""
    print filtered






    document_1_text = 'This is document one'
    document_2_text = 'This is document two'

    document_1_words = document_1_text.split()
    document_2_words = document_2_text.split()

    common = set(document_1_words).intersection( set(document_2_words) )
    unique = set(document_1_words).symmetric_difference( set(document_2_words) )


    print "document 1 : " +document_1_text
    print "document 2 : " +document_2_text
    print "Common: "+str(len(common))
    print "       "+str(common)
    print "Unique: "+str(len(unique))
    print "       "+str(unique)

if __name__ == '__main__':
    main()
