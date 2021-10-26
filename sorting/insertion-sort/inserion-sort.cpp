#include <iostream>
#include <vector>

using namespace std;

vector<int> InsertionSort (vector<int>& input) {

  for (int i = 1; i < input.size(); ++i) {

    int current_num = input[i];
    int j = i;

    while(j > 0 && current_num < input[j-1]) {

      input[j] = input[j-1];
      j--;
    }

    input[j] = current_num;
  }

  return input;
}

int main() {
	
  cout << "Insertion sort test" << endl; 
  
  vector<int> input{1,1,2,4,3,0,1,2,3,1};

  cout << "Input" << endl;
  
  for (auto num : input) {
      cout << num << ","; 
  }
  cout << endl;

 auto output = InsertionSort(input);

  cout << "Output" << endl;

  for (auto num : output) {
      cout << num << ",";
  }

  cout << endl;
	
}