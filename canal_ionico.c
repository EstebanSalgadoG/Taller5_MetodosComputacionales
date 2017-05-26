#include <stdlib.h>
#include <stdio.h>
#include <math.h>

double distancia_Centros(double x0,double y0, double x1, double y1);
double radio_minimo(double x0,double y0, double *x, double *y, int n);
int main(void){
	double *x;
	double *y;
	double x_nuevo; //nueva posicion x
	double y_nuevo; //nueva posicion y
	double x0=0;
	double y0=0;
	double r_nuevo; //radio nuevo
	double r0;//radio anterior
	double beta; //variable para aceptar algunos errores.
	
	int n=42;
	FILE *data;
	FILE *data1;
	int i;
	double paso=0.7;
	int iter=3000;
	double likelihood;
	
	x=malloc(42*sizeof(double));
	y=malloc(42*sizeof(double));
	
	data=fopen("Canal_ionico.txt","r");
	for(i=0;i<n;i++){
		fscanf(data,"%lf %lf\n",&x[i],&y[i]);
		
	}
	r0=radio_minimo(x0,y0,x,y,n);
	for(i=0; i<iter;i++){
		
		x_nuevo=x0+(drand48()*2.0*paso)-paso;
		y_nuevo=y0+(drand48()*2.0*paso)-paso;
		r_nuevo=radio_minimo(x_nuevo, y_nuevo,x,y, n); //calcula el nuevo radio
		likelihood=r_nuevo/r0;
		if (likelihood>1.0){
			x0=x_nuevo;
			y0=y_nuevo;
			r0=r_nuevo;
		}
		
		else{
			//Regla para que se acepten algunos casos diferentes
			//Tomado de https://github.com/ComputoCienciasUniandes/MetodosComputacionales/blob/master/notes/14.MonteCarloMethods/bayes_MCMC.ipy_nuevob
			beta=drand48();
			if(beta<likelihood){
				x0=x_nuevo;
				y0=y_nuevo;
				r0=r_nuevo;
			}
		}
	printf("%lf %lf %lf\n", x0,y0,r0);	
	}
	
	
}
double distancia_Centros(double x0,double y0, double x1, double y1){
	//calcula la distancia entre dos el centro del posible poro y una particula.
	double cuadrados=(pow(x0-x1,2))+(pow(y0-y1,2));
	return pow(cuadrados,0.5);
}

double radio_minimo(double x0,double y0, double *x, double *y, int n){ 
	//Calcula el radio más grande que puede tener el poro sin tocar los puntos mas cercanos.
	double r=distancia_Centros(x0, y0, x[0], y[0]);
	double dis;
	for (int i=0; i<n;i++){
		dis=distancia_Centros(x0, y0, x[i], y[i]);
		if(dis<r){
			r=dis;
		}
	}
	return r-1; //-1 ya que este es el radio ionico de cada particula.
}
