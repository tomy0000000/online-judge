//
//  main.cpp
//  100 - The 3n + 1 problem
//
//  Created by Tomy Hsieh on 2018/12/18.
//  Copyright © 2018 Tomy Hsieh. All rights reserved.
//

#include <iostream>
using namespace std;

unsigned long long three_n_plus_one(unsigned long long n) {
  unsigned long long cnt = 1;
  while (n != 1) {
    n = (n%2 == 1) ? 3*n+1 : n/2;
    cnt++;
  }
  return cnt;
}

int main(int argc, const char * argv[]) {
  unsigned long long a, b, cur_max = 0;
  while (cin >> a >> b) {
    cur_max = 0;
    cout << a << " " << b << " ";
    for (unsigned long long i=min(a, b); i<=max(a, b); i++) {
      cur_max = max(cur_max, three_n_plus_one(i));
    }
    cout << cur_max << endl;
  }
}
