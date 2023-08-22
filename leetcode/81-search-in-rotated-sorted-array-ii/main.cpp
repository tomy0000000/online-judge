// Let n be the length of nums
//
// Time: O(n)
// Space: O(1)

#include <iostream>
#include <vector>

using std::vector;

class Solution {
  public:
    bool search(vector<int> &nums, int target) {
        int start = 0;
        int end = nums.size() - 1;
        while (true) {
            if (nums[start] == target or nums[end] == target) {
                return true;
            }
            start += 1;
            end -= 1;
            if (end < start) {
                return false;
            }
        }
    }
};
