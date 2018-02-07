#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    unsigned long long int n; 
    scanf("%lld",&n);
    unsigned long long int p;
    scanf("%lld",&p);
    unsigned long long int maxTurns = n / 2;
    unsigned long long int frontTurns = p / 2;
    unsigned long long int backTurns = maxTurns - frontTurns;
    if (backTurns > frontTurns) {
        printf("%lld", frontTurns);
    } else {
        printf("%lld", backTurns);        
    }    
    return 0;
}