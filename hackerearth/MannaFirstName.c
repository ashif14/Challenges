#include <stdio.h>
#define MAX 150
int main() {
    int tc;
    scanf("%d",&tc);
    char firstname[] = "SUVO";
    char lastname[] = "JIT";
    int firstname_l = strlen(firstname);
    int lastname_l = strlen(lastname);
    while(tc--) {
        char str[MAX];
        scanf("%s", &str);
        int str_l = strlen(str);
        printf("%d",lastname_l);
        int suvo_count = 0;
        int suvojit_count = 0;
        int i=0;

        while(i< str_l - firstname_l +1) {
            int found_suvo = 1;
            int found_suvojit = 1;
            int j;
            for(j=0;j<firstname_l;j++)
                if(str[i+j] != firstname[j])
                    found_suvo = 0;
            for(j=0;j<lastname_l; j++)
                if(str[i+firstname_l+j] != lastname[j])
                    found_suvojit = 0;
            if(found_suvojit){
                suvojit_count+=1;
                i+=7;
                found_suvo = 0;
            } else if(found_suvo){
                suvo_count+=1;
                i+=4;
                found_suvojit = 0;
            } else {
                i+=1;
            }
        }
        printf("SUVO = %d, SUVOJIT = %d\n",suvo_count,suvojit_count);
    }
    return 0;
}

