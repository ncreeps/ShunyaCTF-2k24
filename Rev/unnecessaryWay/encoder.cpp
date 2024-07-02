#include<iostream>
#include<string>
#include<math.h>
#include<fstream>
using namespace std;

string FLAG;
unsigned int key = 69;

void encrypt(string& flag, int pos){
    if(pos >= floor(flag.length() / 2)){
        return;
    }
    
    flag[pos] = flag[pos] ^ flag[flag.length() - pos - 1];
    flag[flag.length() - pos - 1] = flag[flag.length() - pos - 1] ^ key;

    pos++;

    encrypt(flag, pos);
}


int main(int argc, char *argv[]){
    string FLAG(argv[1]);
    for(int i = 0; i < FLAG.length(); i++){
        cout << (int) FLAG[i] << " ";
    }
    cout << endl;

    encrypt(FLAG, 0);
    for(int i = 0; i < FLAG.length(); i++){
        cout << (int) FLAG[i] << " ";
    }
    cout << endl;
    
    ofstream out("flag", ios::out | ios::binary);


        out.write(FLAG.c_str(), FLAG.length());

    out.close();

    return 0;
}