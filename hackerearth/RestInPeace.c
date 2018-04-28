int main() {
    int n,i, j, found=0, num_j,r;
    int idx_two, idx_one;
    scanf("%d",&n);

    int num_ar[n];

    for(i=0;i<n;i++)
        scanf("%d",&num_ar[i]);

    for(i=0;i<n;i++) {
        found = 0;
        j = 0;
        idx_two = -1;
        idx_one = 1000;
        if(num_ar[i]%21==0) {
            found = 1;
        } else {
            num_j = num_ar[i];
            while(num_j > 0){
                r = num_j%10;
                if(r == 1 && (num_j/10)%10 ==2)
                    found = 1;
                num_j = num_j/10;
                j++;
            }
        }
        if(found ==1 ) {
            printf("The streak is broken!\n");
        } else {
            printf("The streak lives still in our heart!\n");
        }
    }
}
