#include<stdio.h>

int main(){
    int n,i,j, min, days, power;
    scanf("%d",&n);
    scanf("%d",&days);

    long int ar[n];
    for(i=0;i<n;i++){
        scanf("%d",&ar[i]);
        if(ar[i] < min)
            min = ar[i];
    }
    power = min;
    for(i=0;i<days;i++){
        if(i==0)
        for(j=0;j<n;j++)
            if(ar[j] <=power)
                ar[j]-= power;
        else{
            // decreasing power first
            for(j=0;j<n;j++) {
                // if house is alredy destroyed
                if(ar[j] == 0){
                    // destroy house at distance day i
                    ar[j+i]-=power;
                }
                // if this is last day
                if(i == days -1) {
                    power = ar[j];
                    ar[j] -= power;
                }else if(i>1){
                    ar[j] -= power+1;
                }else {
                    ar[j] -= power;
                }
            }   
        }
    }
    printf("%d\n",power);
}