#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

 long long int calculateNimSum(long long int piles[], int n)
{
    long long int i, nimsum;
     if (piles[0] > 0) {
        nimsum = piles[0] +1;    
     } else {
         nimsum = piles[0];
     }
     
    for (i=1; i<n; i++){
        if (piles[i] > 0){
            nimsum = nimsum ^ ( piles[i] +1);
        } else {
            nimsum = nimsum ^ ( piles[i]);
        }
    }
        
     
     //printf("nimsum-%lld\n",nimsum);
    return(nimsum);
}

void makeMove(long long int piles[], int n) {
    
     long long int i, nim_sum = calculateNimSum(piles, n);
    
  
    for (i=0; i<n; i++) {
        if ((piles[i] ^ nim_sum) < piles[i]) {
            piles[i] = (piles[i] ^ nim_sum);
            break;
        }
     }

}
 

int main(){
    int g; 
    scanf("%d",&g);
    for(int a0 = 0; a0 < g; a0++){
        int n; 
        int x;
        scanf("%d",&n);
        long long int *p = malloc(sizeof( long long int) * n);
        for(int p_i = 0; p_i < n; p_i++){
           scanf("%lld",&p[p_i]);
        }
        int aa = 0;
        int player_turn = 1;
         if (calculateNimSum(p, n) !=0) {
             aa = 1;
             printf("W\n");
             continue;
         } 
       
        for (int i = 0; i < n; i++) {
            makeMove(p,n);
            if (player_turn == 1) player_turn = 0;
            if (player_turn == 0) player_turn = 1;
            if ((calculateNimSum(p, n) !=0) && (player_turn == 1)) {
                printf("W\n");  
                aa = 1;
                break;
            } 
        }
        
        if (aa == 0) {
            printf("L\n");
        }
    }
    return 0;
}
