#include <bits/stdc++.h>
#include <stdio.h>
// Number of array max is MAX_SIZE.
using namespace std;
#define MAX_SIZE 500
/*
    Have algorithms irrelevant sort array.
    + Insert sort (Sắp xếp chèn)
    + Bubble sort (Sắp xếp nổi bọt)
    + Selection sort (Sắp xếp chọn)
    + Merge sort (Sắp xếp trộn)
    + Quick sort (Sắp xếp nhanh)
    + Heap sort (Sắp xếp vun đống)
*/
void menu()
{
    cout<<"======== Choose algorithms sort array ========"<<endl;
    cout<<"         1. Insert sort."<<endl;
    cout<<"         2. Selection sort."<<endl;
    cout<<"         3. Bubble sort."<<endl;
    cout<<"         4. Merge sort."<<endl;
}
//
void Insert_sort(int a[], int size)
{
    int pos , temp;
    for(int i = 1 ; i < size ; i++)
    {
        temp = a[i];
        pos = i;
        while((pos > 0) && (a[pos-1] > temp))
        {
            a[pos] = a[pos - 1];
            pos = pos - 1;
        }
        a[pos] = temp;
    }
}
//
void Selection_sort(int a[], int size)
{
    int index_min,temp;
    for(int i = 0 ; i < size - 1 ; i++)
    {
        index_min = i;
        for(int j = i + 1; j < size; j++)
        {
            if(a[j] < a[index_min]) 
                index_min = j;
            temp = a[i];
            a[i] = a[index_min];
            a[index_min] = temp;
        }
    }
}
//
void Bubble_sort(int a[], int size)
{
    
}
//
void Merge_sort()
{

}
//
int main()
{
    int n; // Number of array express keyboard.
    char k;
    cin >> n;
    int A[n];
    if(n > MAX_SIZE)
        cout<<"Programs is error";
    else
    {
        do
        {
            for(int i = 0 ; i < n ; i++)
            {
                cout<<"Express element "<<i+1<<" of array: ";
                cin >> A[i];
            }
            menu();
            switch(4)
            {
                case 1 : Insert_sort(A,n); break;
                case 2 : Selection_sort(A,n); break;
                case 3 : Bubble_sort(A,n); break;
                case 4 : Merge_sort(); break;
            }
            cout<<"Do you want to continue program??? Express Y/y to continue.";
            k = getchar();
        } while (k == 'Y' || k == 'y');
        
    }
}