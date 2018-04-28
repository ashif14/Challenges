#include<stdio.h>

int main() {
    int tc, i, s,k,j, count, step, last_thief , last_police;
    scanf("%d",&tc);
    char ar[1001][1001] = {0};
    char c;

    while(tc--) {
        scanf("%d %d\n", &s,&k);
        
        for(i=0;i<s;i++)
            for(j=0;j<s; j++) {
                scanf("%c%c",&ar[i][j],&c);
            }
            count = 0;
            char visited[1001][1001] = {0};

            for(i=0;i<s;i++) {
                j = 0;
                last_thief = 0;
                last_police = 0;
                while(j<s) {
                    if(ar[i][j] == 'P' && !visited[i][j]){
                        step = last_thief +1>j?last_thief+1:j+1;
                        while(step < j+k+1 && step < s){
                            if(ar[i][step] == 'T' && visited[i][step] == 0){
                                last_thief = step;
                                visited[i][step] = 1;
                                count++; 
                                break;
                            }
                            step++;
                        }
                    }

                    if(ar[i][j] == 'T' && !visited[i][j]) {
                        step = last_police + 1>j?last_police+1:j+1;
                        while(step < j+k+1 && step < s) {
                            if(ar[i][step] == 'P' && visited[i][step] == 0) {
                                last_police = step;
                                visited[i][step] = 1;
                                count++; 
                                break;
                            }
                            step++;
                        }
                    }
                    j++;
                }
            }

            printf("%d\n",count);
        }
    }
