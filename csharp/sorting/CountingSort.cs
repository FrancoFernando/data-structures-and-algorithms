namespace Algorithms.Sorting
{
    public class CountingSort<T> : IIntegerSorting<T>
    {
        public (int key, T val)[] Sort((int key, T val)[] arr)
        {
            int maxKey = arr.Max(x => x.key);
            int minKey = arr.Min(x => x.key);

            var frequencies = new Dictionary<int,int>();
            foreach(var item in arr) {
                if(frequencies.ContainsKey(item.key))
                    frequencies[item.key]++;
                else
                    frequencies[item.key] = 1;
            }

            int counter = 0;
            for(int k = minKey; k <= maxKey; ++k) {
                if(frequencies.ContainsKey(k)) {
                    frequencies[k] += counter; 
                    counter = frequencies[k];
                }
            }

            var outputArr = new (int key, T val)[arr.Length];

            for(int i = arr.Length-1; i >= 0; --i) {
                outputArr[--frequencies[arr[i].key]] = arr[i];
            }

            return outputArr;
        }
    }
}
