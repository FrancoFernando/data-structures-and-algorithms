#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

vector<int> SelectionSort(vector<int> input) {
  
	for (int i = 0; i < input.size()-1; ++i) {
      
			int smallest_index = i;
      
			for (int j = i+1; j < input.size(); ++j) {
              
				if (input[j] < input[smallest_index]) {
                  
                	smallest_index = j;
                }
			}
			swap(input[i], input[smallest_index]);
		}
		return input;
}



int main() {
	
  cout << "Selection sort test" << endl; 
  
  vector<int> input{1,1,2,4,3,0,1,2,3,1};

  cout << "Input" << endl;
  
  for (auto num : input) {
      cout << num << ","; 
  }
  cout << endl;

 auto output = SelectionSort(input);

  cout << "Output" << endl;

  for (auto num : output) {
      cout << num << ",";
  }

  cout << endl;
	
}