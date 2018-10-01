// https://practice.geeksforgeeks.org/problems/the-celebrity-problem/1
// ----------- Description -------------------
// You are in a party of N people, where only one person is known to everyone. Such a person may be present in the party, if yes, (s)he doesn’t know anyone in the party. Your task is to find the stranger (celebrity) in party.
// You will be given a square matrix M where if an element of row i and column j  is set to 1 it means there is an edge from ith person to jth person. An edge represent the relation that i th person knows j th person. You need to complete the function getId which finds the id of the celebrity if present else return -1. The function getId takes two arguments the square matrix M and its size n.

// Input:
// The first line of input contains an element T denoting the No of test cases. Then T test cases follow. Each test case consist of 2 lines. The first line of each test case contains a number denoting the size of the matrix M. Then in the next line are space separated values of the matrix M.
 
// Output:
// For each test case output will be the id of the celebrity if present (0 based index). Else -1 will be printed. 

// Example:
// Input (To be used only for expected output) 
// 1
// 3
// 0 1 0 0 0 0 0 1 0

// Output 
// 1

// Explanation 
// For the above test case the matrix will look like
// 0 1 0 
// 0 0 0
// 0 1 0
// Here  the celebrity is the person with index 1 ie id 1 

// ----------- Description -------------------


// --------- included code -------------------
{
#include<bits/stdc++.h>
using namespace std;
#define MAX 100
int getId(int M[MAX][MAX],int n);
int main()
{
    int T;
    cin>>T;
    int M[MAX][MAX];
    while(T--)
    {
        int N;
        cin>>N;
        memset(M,0,sizeof M);
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<N;j++)
            {
                cin>>M[i][j];
            }
        }
        cout<<getId(M,N)<<endl;
    }
}

}
// ------------ end included code ----------------

/*Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above.*/

// The task is to complete this function
int getId(int M[MAX][MAX], int n)
{
    // stranger holds the index for the celebrity 
    int stranger = -1;
    // isCelebPresent is a flag to determine if there is a celeb or not
    bool isCelebPresent = false;
    
    // if all 0's then return id
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
	    // if matrix value contains a 1, a celebrity is present
	    // there is no need to check the rest of the row
            if(M[i][j] == 1){
                isCelebPresent = true;
                break;
            }
	    // check if j hit the end of the row
	    // if end of row and stranger hasn't been set before set stranger
	    // if stranger has been set before, no celebrity is present
            if(j == n-1){
                if(stranger != -1){
                    return -1;
                }
                stranger = i;
            }
        }
    }
    // check if celeb present and that stranger was set
    // otherwise return -1 for no celebrity present
    if(isCelebPresent && stranger != -1){
        return stranger;
    }else{
        return -1;
    }
}