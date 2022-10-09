#include<stdio.h>
void printArray(int* arr, int size){
    for (int i = 0; i < size; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
}
void insertionSort(int *arr, int size){
    int key, j;
    for (int i = 1; i <= size-1; i++)
    {
        key = arr[i];
        j = i-1;
        while(j>=0 && arr[j] > key){
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = key;
    }
}

void main(){
    int arr[] = {12, 54, 65, 7, 23, 9};
    int size = sizeof(arr)/sizeof(arr[0]);
    printArray(arr, size);
    insertionSort(arr, size);
    printArray(arr, size);
}
