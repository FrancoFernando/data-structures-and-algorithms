#include <cmath>

//Extract a specific digit from a number
int ExtractDigits(int num, int digit) {
	int digit_column = pow(10, digit);
	return (num / digit_column) % 10;
}

// Simple Math
int CountDigits(int num) {
	
	int digits = 0;
	while (num > 0) {
		num /= 10;
		digits++;
	}
	return digits;
}

// Logarithms
int CountDigitsWithLog(int num) {	
	return floor(log10(n) + 1);
}

// Strings
int CountDigitsWithString(int num)
{
    string s = to_string(num);
    return s.size(); 
}
