from nltk.corpus import stopwords

def main():

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
    print filtered



    print ""
    print ""
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
