#include <vector>
#include <algorithm>
using namespace std;

int CountDigits(int num) {
	
	int digits = 0;
	while (num > 0) {
		num /= 10;
		digits++;
	}
	return digits;
}

vector<int> CountingSort(vector<int> array, int digit_position) {
	
	const int base = 10;
	int bookkeeping[base]= {0};
	
	int digit_column = pow(10, digit_position);
	
	for(int num : array) {
		int digit = (num/digit_column) % base;
		bookkeeping[digit]++;
	}
	
	partial_sum(&bookkeeping[0], &bookkeeping[base], &bookkeeping[0]);
	
	vector<int> output(array.size());

	for (int i = array.size()-1; i >= 0; --i) {
		int curr_digit = (array[i]/digit_column) % base;
		output[--bookkeeping[curr_digit]] = array[i];
	}
	return output;
}



vector<int> RadixSort(vector<int> array) {
  
	if (array.empty()) return {};

	int max_num = *max_element(array.begin(), array.end());
	
	int max_digits = CountDigits(max_num);
	
	for (int i = 0; i < max_digits; ++i) {
		array = CountingSort(array, i);
	}
	
	return array;
}


int main() {
	
  cout << "Radix sort test" << endl; 
  
  vector<int> input{8762, 654, 3008, 345, 87, 65, 234, 12, 2};

  cout << "Input" << endl;

  
  for (int num : input) {
    cout << num << endl;
  }

  vector<pair<int, string>> output = RadixSort(input);

  cout << "Output" << endl;

  for (auto item : output) {
    cout << num << endl;
  }
	
}