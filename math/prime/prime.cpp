#include <cmath>
#include <vector>

using namespace std;

bool IsPrimeBruteForce (int n) {

    for (int i = 2; i < n; i++) {
        if (n % i == 0) {
            return false;
        }
    }

    return true;
}

bool IsPrime(int n) {

  if (n == 2) return true;
  if (n <= 1 || n % 2 == 0) return false;
  
  int m = sqrt(n);

  for (int i = 3; i <= m; i += 2) {
        if (n % i == 0) {
            return false;
        }
  }

  return true;
}

vector<bool> Sieve(int n) {

  vector<bool> prime(n + 1, true);
  prime[0] = false;
  prime[1] = false;

  int m = sqrt(n);

  for (int i = 2; i <= m; i++) {
      if (prime[i]) {
        for (int j = i * i; j <= n; j += i) {
            prime[j] = false;
        }           
    }
  }
    
  return prime;
}

