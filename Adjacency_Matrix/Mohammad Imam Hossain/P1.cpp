//underacted adjacency_matrix
// Created by Sifat Ali on 1/13/2024.
//

#include <iostream>
#include <fstream>

using namespace std;

int main(){

    int adj_mat[100][100]={0};


    ifstream fileobj;
    fileobj.open("E:\\DSA 2\\Graph\\Mohammad Imam Hossain\\Graph.txt",ios::in);

    if(fileobj.is_open()){
        int node,edges;
        fileobj>>node>>edges;
        for (int i = 0; i < edges; ++i) {
            int firstnode,secondnode;

            fileobj>>firstnode>>secondnode;
            adj_mat[firstnode][secondnode]=1;
            adj_mat[secondnode][firstnode]=1;
        }

        for (int row = 1; row <=6 ; ++row) {
            for (int col = 1; col <=6 ; ++col) {
             cout<<adj_mat[row][col]<<" ";
            }
            cout<<endl;
        }

    }
    else{
        cout<<"Error File is not open"<<endl;
    }
}
