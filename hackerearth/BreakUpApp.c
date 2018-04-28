#include<stdio.h>
#define MESSAGE_MAX 1000
int main() {
    int chat_length;
    scanf("%d", &chat_length);
    int date_girl_count = 0;
    int date_menot_count = 0;
    int nodate_girl_count = 0;
    int nodate_menot_count = 0;
    
    while(chat_length-- + 1 ){
        char message[MESSAGE_MAX];
        gets(message);

        int message_length = strlen(message);

        int i = 0;
        int date = 0;
        int isGirlMsg = 0;
        int isMenotMsg = 0;

        if(message[0] == 'G')
            isGirlMsg = 1;
        else
            isMenotMsg = 1;
        while (i < message_length) {
            date = 0;
            if( message[i] >= '0'  && message[i] <= '9'){
                date = (message[i] - '0')* 10;
                date += message[i+1] - '0';
                i+=2;
                if(isGirlMsg && (date== 19 || date == 20) )
                    date_girl_count+=1;
                else if(isMenotMsg && (date == 19 || date == 20))
                    date_menot_count+=1;
                else if(isGirlMsg){
                    nodate_girl_count+=1;
                }else
                    nodate_menot_count+=1;
            }else {
                i+=1;
            }
        }
    }
    if(date_girl_count*2 > nodate_girl_count*2 && date_menot_count > nodate_menot_count || (date_girl_count*2 + date_menot_count) > (nodate_girl_count*2 + nodate_menot_count))
        printf("Date\n");
    else
        printf("No Date\n");
}
