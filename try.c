#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#define PI 3.13159


int main(void){
//	try1();
//	imprimir();
//	principal();
//	arrays();
//	vArray();
//	ifdo();
	hacerlinea(0,10,10);
	return 0;
}

int hacerlinea(int pInicio, int pFin, int pCantidad)
{
	float *lista;
	lista = malloc(pCantidad*sizeof(int));
	float p=pInicio;
	float paso=(pFin-pInicio)/pCantidad;
	lista[0]=p+paso;


	for(i=0;i<pCantidad;i++){
		lista[i]=p+paso;
		p=p+paso;
	}
	for (i=0;i<pCantidad;i++){
		printf("%f\n", lista[i]);
	}

}
/*
int imprimir(void){

	FILE*in;
	int i;
	int var;
	int test;
	char filename[100]="new_data.dat";
	printf("Writing to file %s\n", filename);
	
	in =fopen(filename,"w");

	if(!in){
	printf("problems opening the %s\n", filename);
	exit(1);
	}


	for(i=0;i<10;i++){
	fprintf(in, "%d\n",i)
	}
	
	fclose(in);


	return 0;
}

*/
int try1(void){
	int a;
	int b;
	int c;
	
	float d;
	float e;
	float f;

	a=1;
	b=10;
	c=pow(a,b);

	d=1.0;
	e=10.0;
	f=pow(a,b);

	printf("Hello World\n");
	printf("%d %d %d \n",a,b,c);
	printf("%f %f %f \n",d,e,f);

}

int imprimir(void){
	char s[100]="La respuesta es:";
	char i=42;
	float x=42.0;
	double y=42.0;
	printf("%s\n %e", s,y);
	return 0;

}

int principal(void){

	int i;
	float radius;
	float volume;
	float surface;

	radius=0.0;
	volume=0.0;
	surface=0.0;

	printf("Radius Surface Volume\n");
	for(i=0;i<12;i++){
		radius=i;
		surface=4.0*PI*radius*radius*radius;
		printf("%f %f %f\n", radius, surface, volume);
	}
	return 0;	
	
}	

int arrays(void){
	int lista[10];
	int i;
	printf("Content before initialization\n");
	
	for(i=0;i<10;i++){
	printf("%d\n",lista[i]);	
	}
	
	//initialize
	for(i=0;i<10;i++){
	lista[i]=i*2;
	}
	//print new content
	printf("Content after initialization\n");
	for(i=0;i<10;i++){
		printf("%d\n", lista[i]);
	}
	return 0;


}

int vArray(void){
	int i;
	//future arrays
	int *array_int;
	
	int n_points;
	n_points=10;

	array_int = malloc(n_points*sizeof(int));

	//check if everything went OK
	if (!array_int){
		printf("There is something wrong with array\n");
		exit(1);
	}

	printf("Memory starts at %p\n", array_int);

	//fill array with data
	printf("allocation went Ok. initializing...\n");
	for (i=0;i<n_points;i++){
		array_int[i] = i*2;
		printf("%d\n", array_int[i]);
	}

	printf("Let's see what happens if i go beyond the allocated space ...\n");

	array_int[n_points] = n_points*2;
	printf("%d\n", array_int[n_points]);
	printf("OK.\n");

	//What if i go far away?
	printf("and if i go far away? \n");
	array_int[n_points*10000]=n_points*10000*2;
	printf("%d\n",array_int[n_points*10000]);
	
	printf("everything went just fine\n");
	return 0;
	

}
/*
int Strings(void){
	char name[256];
	char lastname[256];
	char fullname[256];
	int year;

	printf("Garbage in string name %s\n",name);
	printf("Garbage in string lastname %s\n", lastname);
	
	strcpy(name, "Simon");
	strcpy(lastname, "El bobito");
	printf("After initialization: %s %s\n",name, lastname);
	tear=1965;
	sprintf(fullname, "%s,%s; Born %d", lastname,name, year);
	
	printf("Final string: %s\n",fullname);
	return 0;

}*/

int ifdo(void){
	int a;
	int b;
	
	a=1;
	b=2;

	if(a>b){
		printf("a is greater than b: a=%d, b=%d\n",a,b);
	}

	//if else
	a=1;
	b=1;
	if(a<b){
		printf("a is greater than b: a=%d, b=%d\n",a,b);
	}	
	else{
		printf("a is equal or greater than b: a=%d, b=%d\n",a,b);
	}

	printf("A loop with do-while structure\n");

	a=0;
	b=10;
	do{
		printf("a=%d, b=%d\n",a,b);
		a++;
	}while(a<b);

	return 0;
	

}



/*	cc try.c -lm -o try.x
	./try.x
*/
