//Firend Pairing Problem:
//Given n friends,each one can remain single or can be paired up with onefriends.
//
//Each friend can be paired only once.Find out the total number of ways in
//which friends can remain singal or can be paired up.
//
// Created by Sifat Ali on 1/11/2024.
//
//---------------------------------
//expalin {1,2,3,4,5,6,7,8,9,10}
//
//way1: remain single. friend={1,2,3,4,5,6,7,8,9}group from
//
// way2 : remain mingle : no of ways :9
//                                 friend no of way:9-1
//                                         friend no of way :9-2
//                                               .
//                                               .
//                                              9-n
//    total way=way1+way2;
//---------------------------------

#include <iostream>

using namespace std;

int friend_pair(int n){
    if(n==1){
        return 1;
    }
    else if(n==2){
        return 2;
    }
    else{
        int way1= friend_pair(n-1);

        int way2= (n-1)*friend_pair(n-2);
        return way1+way2;
    }
}

int main(){
    cout<<"Ways"<<friend_pair(10)<<endl;
}

