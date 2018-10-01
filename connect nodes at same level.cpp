// https://practice.geeksforgeeks.org/problems/connect-nodes-at-same-level/1
//
// ----------------------------------------------
// Write a function to connect all the adjacent nodes at the same level in a binary tree. Structure of the given Binary Tree node is like following.
 
// struct Node{
//  int data;
//  Node* left;
//  Node* right;
//  Node* nextRight; 
// }

// Example:

// Input Tree
//       10
//      / \
//     3   5
//    / \   \
//   4   1   2


// Output Tree
//       10--->NULL
//      / \
//     3-->5-->NULL
//    / \   \   
//   4-->1-->2-->NULL
// Initially, all the nextRight pointers point to garbage values. Your function should set these pointers to point next right for each node.
//
// Input:
// The task is to complete the method which takes one argument, root of Binary Tree. There are multiple test cases. For each test case, this method will be called individually.

// Output:
// The function should update nextRight pointers of all nodes.
//
// Example:
// Input:
// 2
// 2
// 3 1 L 3 2 R
// 4
// 10 20 L 10 30 R 20 40 L 20 60 R

// Output:
// 3 1 2
// 1 3 2
// 10 20 30 40 60
// 40 20 60 10 30
// ----------------------------------------------

{
#include <bits/stdc++.h>
using namespace std;
struct Node
{
  int data;
  struct Node *left;
  struct Node *right;
  struct Node *nextRight;
};
void connect(struct Node *p);
/* Helper function that allocates a new node with the
   given data and NULL left and right pointers. */
struct Node* newNode(int data)
{
  struct Node* node = new Node;
  node->data = data;
  node->left = NULL;
  node->right = NULL;
  return(node);
}
void printSpecial(Node *root)
{
   if (root == NULL)
     return;
   Node *node = root;
   while (node != NULL)
   {
      printf("%d ", node->data);
      node = node->nextRight;
   }
   if (root->left)
     printSpecial(root->left);
   else
     printSpecial(root->right);
}
void inorder(Node *root)
{
    if (root == NULL)
       return;
    inorder(root->left);
    cout << root->data << " ";
    inorder(root->right);
}
/* Driver program to test size function*/
int main()
{
  int t;
  scanf("%d
", &t);
  while (t--)
  {
     map<int, Node*> m;
     int n;
     scanf("%d",&n);
     struct Node *root = NULL;
     struct Node *child;
     while (n--)
     {
        Node *parent;
        char lr;
        int n1, n2;
        scanf("%d %d %c", &n1, &n2, &lr);
        if (m.find(n1) == m.end())
        {
           parent = newNode(n1);
           m[n1] = parent;
           if (root == NULL)
             root = parent;
        }
        else
           parent = m[n1];
        child = newNode(n2);
        if (lr == 'L')
          parent->left = child;
        else
          parent->right = child;
        m[n2]  = child;
     }
     connect(root);
     printSpecial(root);
     printf("
");
     inorder(root);
     printf("
");
  }
  return 0;
}

}

/*Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above.*/

/* struct Node
{
  int data;
  Node *left,  *right;
  Node *nextRight;  // This has garbage value in input trees
}; */
// Should set the nextRight for all nodes
void connect(Node *p)
{
    //INPUTS
    //4
    //10 20 L 10 30 R 20 40 L 20 60 R
    
    //OUTPUTS
    //10 20 30 40 60
    //40 20 60 10 30
    
    if(p == NULL){
        return;
    }
    
    queue<Node*>q;
    q.push(p);

    while(!q.empty())
    {
        int size=q.size();
        Node* prev=NULL;

        while(size--)
        {
            Node* temp=q.front();
            q.pop();
            
            if(temp->left)
            q.push(temp->left);
            if(temp->right)
            q.push(temp->right);
            
            if(prev!=NULL)
            prev->nextRight=temp;
            
            prev=temp;
        }

        prev->nextRight=NULL;
    }
}