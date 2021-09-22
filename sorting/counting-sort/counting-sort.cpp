template <typename T>
using value_type = pair<const int, T>;

vector<value_type> countingSort (vector<value_type> const& inputs, int maxKey) {

  vector<int> bookkeeping(maxKey+1, 0);
  
  //count keys frequency
  for (const auto& input : inputs) {
      bookkeeping[input.first]++;
  }

  //at the end each element is the index of the last element with that key
  std::partial_sum(bookkeeping.begin(), bookkeeping.end(), bookkeeping.begin());

  vector<value_type> output(inputs.size());

  //build sorted output iterating backward
  for (auto it = inputs.crbegin(); it != inputs.crend(); ++it) {
        output[--bookkeeping[it->first]] = *it; 
  }

  return output;
}