#include "utils.h"

String array2String(int* arr, uint16_t arr_len, String separator){
    uint8_t i;
    String s = String(arr[0]);
    for (i = 1; i < arr_len; i++){
        s = s + separator + String(arr[i]);
    }
    return s;
}