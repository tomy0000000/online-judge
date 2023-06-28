#include <iostream>
#include <map>
using namespace std;

int main() {
  int num;
  while (cin >> num) {
    map<int, int> D;
    while (num != 1) {
      int init = 2;
      while (num%init != 0) {
        init++;
      }
      D[init] = (D.find(init) != D.end()) ? D[init] + 1 : 1;
      num /= init;
    }
    for (map<int, int>::iterator it = D.begin(); it != D.end();) {
      cout << it->first;
      if (it->second != 1) {
        cout << "^" << it->second;
      }
      it++;
      if (it != D.end()) {
        cout << " * ";
      }
    }
    cout << endl;
  }
}
