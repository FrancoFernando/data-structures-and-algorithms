#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <numeric>

using namespace std;

//Only keys
void CountingSort(vector<int>& keys) {

    int max_key = *max_element(keys.begin(), keys.end());

    vector<int> bookkeeping(max_key + 1);

    for (int key : keys) bookkeeping[key]++;

    for (int i = 0, k = 0; i <= max_key; ++i) {
        for (int j = 0; j < bookkeeping[i]; ++j) {
            keys[k++] = i;
        }
    }
}

//Without space Optimization
/*
vector<pair<int, string>> CountingSort(vector<pair<int, string>>& items) {

    int max_key = max_element(items.begin(), items.end(), [](auto const& x, auto const& y) {return x.first < y.first; })->first;
    vector<int> bookkeeping(max_key+1, 0);

    //counter[i] corresponds to the number of entries with key equal to i
    for (const auto& item : items) {
        bookkeeping[item.first]++;
    }

    //nextIndex[i] corresponds to the number of entries with key less than i
    vector<int> next_index(max_key+1, 0);
    for (int i = 1; i < next_index.size(); ++i) {
        next_index[i] = next_index[i-1] + bookkeeping[i-1];
    }

    vector<pair<int, string>> output(items.size());
    for (const auto& item : items) output[next_index[item.first]++] = item;

    copy(output.begin(), output.end(), items.begin());
    return output;
}
*/

// With space optimization
vector<pair<int, string>> CountingSort3(vector<pair<int, string>>& items) {

    int max_key = max_element(items.begin(), items.end(), [](auto const& x, auto const& y) {return x.first < y.first; })->first;
    vector<int> bookkeeping(max_key + 1, 0);

    //count keys frequency
    for (const auto& item : items) {
        bookkeeping[item.first]++;
    }

    //at the end each element is the index of the last element with that key
    std::partial_sum(bookkeeping.begin(), bookkeeping.end(), bookkeeping.begin());

    vector<pair<int, string>> output(items.size());

    //build sorted output iterating backward
    for (auto it = items.crbegin(); it != items.crend(); ++it) {
        output[--bookkeeping[it->first]] = *it;
    }

    return output;
}


int main() {
	
  cout << "Counting sort test" << endl; 
  
  vector<int> keys{ 1,1,2,4,3,0,1,2,3,1};

  cout << "Input" << endl;

  vector<pair<int, string>> input{{1,"a"},{1,"b"},{2,"c"},{4,"d"},{3,"e"},{0,"f"},{1,"g"},{2,"h"},{3,"i"},{1,"l"} };
  
  for (auto item : input) {
    cout << "(" << item.first << ", " << item.second << ")" << endl;
  }

  vector<pair<int, string>> output = CountingSort(input);

  cout << "Output" << endl;

  for (auto item : output) {
    cout << "(" << item.first << ", " << item.second << ")" << endl;
  }
	
}