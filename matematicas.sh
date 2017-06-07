wget https://raw.githubusercontent.com/ComputoCienciasUniandes/HerramientasComputacionalesDatos/master/Homework/hw1/01_notas.tsv

touch pasaron.txt

awk '{if($3=="MATEMA" && ($4+$5+$6)/3>=3) print $1}' 01_notas.tsv |wc -l>pasaron.txt
echo "de Matematicas pasaron">>pasaron.txt

