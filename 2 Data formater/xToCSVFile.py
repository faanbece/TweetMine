import string as cadena
import re
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
    outF=open("../Record/Finals/X2Search-OnlyText.csv",'w')


    for line in inp:
        regex= '((?:http[s]?(?:[://])|(?:(?:[a-zA-Z]|[0-9])*[.][a-zA-Z]))(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))*)'

        urls = re.findall(regex, line)

        for url in urls:
            line=line.replace(url,'')

        """
        filtered=line
        filtered= [word for word in filtered if word not in stop]
        line=' '.join(filtered)
        """
        cadena.punctuation.append('...')
        regex = re.compile('[%s]' % re.escape(cadena.punctuation))
        out = regex.sub(' ', line)
        out= ' '.join(out.split())
        outF.write(out.replace(' ',',')+"\n")

if __name__ == '__main__':
    main()
