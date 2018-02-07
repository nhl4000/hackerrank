#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>
int compare( const void* a, const void* b)
{
    long long int int_a = * ( (long long int*) a );
    long long int int_b = * ( (long long int*) b );

     if ( int_a == int_b ) return 0;
     else if ( int_a < int_b ) return -1;
     else return 1;
}


int main(){
    int n; 
    int p; 
    scanf("%d %d",&n,&p);
    long long int *a = malloc(sizeof(long long int) * n);
    for(int a_i = 0; a_i < n; a_i++){
       scanf("%lld",&a[a_i]);
    }
    // your code goes here
    
    qsort( a, n, sizeof(long long int), compare );
    long long int counts = 0;
    long long int sum = 0;
    for(int i = 0; i < n; i++) {
       long long int num_required = (long long int)( a[i] / p);
        if (a[i] % p > 0) {
            num_required++; 
        }
        while (counts >= num_required) {
            num_required++;
        }
        counts = num_required;
        sum = sum + num_required;
    }
    printf("%lld", sum);
    
    return 0;
}