#Saca copia, y elimna las lineas repetidas del archivo, dejando solo un ejemplar de cada una
perl -i.bak -ne 'print if ! $a{$_}++' result-filter.data


sort -us -o data_unique.data data.data
