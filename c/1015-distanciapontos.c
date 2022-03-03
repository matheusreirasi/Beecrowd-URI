#include <stdio.h>
#include <math.h>

int main() {
    double x1,x2,y1,y2,dist;
    scanf("%lf %lf %lf %lf", &x1, &y1, &x2, &y2);
    dist = sqrt(pow(x2-x1, 2)+pow(y2-y1, 2));
    printf("%.4lf\n",dist);
    return 0;
}

//esperava colocar os valores de x1 e y1 em uma linha e x2 e y2 noutra, porém o URI aceitou colocar um em cada linha