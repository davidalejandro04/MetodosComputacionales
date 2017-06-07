
wget https://raw.githubusercontent.com/ComputoCienciasUniandes/HerramientasComputacionalesDatos/master/Homework/hw1/01_notas.tsv
touch pasaroning.txt

awk '{if(substr($3,0,3)=="ING" && ($4+$5+$6)/3>=3) print $1}' 01_notas.tsv |wc -l>pasaroning.txt
echo "de Ingenieria pasaron">>pasaroning.txt

rm 01_notas.tsv
