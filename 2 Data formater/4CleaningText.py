from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
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
    toker = RegexpTokenizer(r'((?<=[^\w\s])\w(?=[^\w\s])|(\W))+', gaps=True)
    inp=open("../Record/Finals/X2Search-OnlyText.data",'r')
    inp2=open("../Record/Finals/X2Search-OnlyText-CLEANED.data",'a')

     for line1 in inp:

         #words1=line1.split(" ")
         words1=toker.tokenize(s)
         words1=[word for word in words1 if word not in stop]




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
