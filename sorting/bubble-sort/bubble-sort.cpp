#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

vector<int> BubbleSort(vector<int> const& input) {

    bool has_swapped = true;
    int iterations = 0, length = input.size();

    while (has_swapped) {

        has_swapped = false;
        for (int i = 0; i < length - iterations - 1; ++i) {
            if (input[i] > input[i + 1]) {
                swap(input[i], input[i + 1]);
                has_swapped = true;
            }
        }
        iterations++;
    }
    return input;
}



int main() {
	
  cout << "Bubble sort test" << endl; 
  
  vector<int> input{1,1,2,4,3,0,1,2,3,1};

  cout << "Input" << endl;
  
  for (auto num : input) {
      cout << num << ","; 
  }
  cout << endl;

 auto output = CountingSort(input);

  cout << "Output" << endl;

  for (auto num : output) {
      cout << num << ",";
  }

  cout << endl;
	
}