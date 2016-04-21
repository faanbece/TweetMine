import string as cadena
import re
import sys
from nltk.corpus import stopwords

def main():
    reload(sys)
    sys.setdefaultencoding('utf8')










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


    print ""
    print ""
    print ""




    print ""
    print ""


    print "   -    "
    string= '####<p>Hello World</p><a href="example.com">More Examples</a><a href="http://example2.com">Even More Examples</a>'
    string+='bit.do 	 Bit.do URL Shortener - Shorten, customize and track your links  t.co 	Twitter URL Shortener  (can not be used outside Twitter) lnkd.in 	lnkd.in is the URL Shortener used by Linked In. db.tt 	 db.tt is the URL Shortener used by Dropbox. Example: https://db.tt/b5gwXppx qr.ae 	Quora uses the  short domain qr.ae when generating external links back to content on Quora. adf.ly 	AdF.ly - The  URL shortener service that pays you! Earn money for every visitor to your '
    """regex= 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    """
    regex= '((?:http[s]?(?:[://])|(?:(?:[a-zA-Z]|[0-9])*[.][a-zA-Z]))(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))*)'

    urls = re.findall(regex, string)


    print urls
    print "   -    "
    print "    -   "
    print "     -  "
    print "      - "


    for url in urls:
        string=string.replace(url,'')

    """ stng = "asd a.sd a.,d.,.2,.,.,s.d,a.sd,a.sdom?=2=)(&&%$)" """
    regex = re.compile('[%s]' % re.escape(cadena.punctuation))
    out = regex.sub(' ', string)
    out= ' '.join(out.split())

    print out

    print ""
    print ""
    print ""

    STOP_TYPES=['DET','CNJ']
    """
    nltk.download('stopwords')
    stop=stopwords.words('english')
    """
    stop=stopwords.words('english')

    sentence="this is ais fothiso bar sentence this is ais fothiso bar sentence this is ais fothiso bar sentence this is ais fothiso bar sentence this is ais fothiso bar sentence this is ais fothiso bar sentence".split(" ")

    filtered="this is ais fothiso bar sentence this is ais fothiso bar sentence this is ais fothiso bar sentence this is ais fothiso bar sentence this is ais fothiso bar sentence this is ais fothiso bar sentence".split(" ")
    filtered= [word for word in filtered if word not in stop]

    print sentence
    print ""

    print ' '.join(filtered)

    """
    Recorrer el arreglo de tweets, y comparar la cantidad de concidencias de un tweet con otro
    solo gardar los 3 o 4 mayores resultados obtenidos al comparar un tweet con otro, actualizar
    (agregarlo o sacarlo de su vector de tweets con mayor coincidencia) ambos tweets cuando uno u otro
    encuentre un tweet con el que guarde mayor coincidencia

    Datos a guardar en el vector de coincidencia:
    Id_srt
    cantidad de palabras concidentes
    palabras coincidentes


    """
if __name__ == '__main__':
    main()
