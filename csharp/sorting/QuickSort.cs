namespace Algorithms.Sorting
{
    public class QuickSort<T> : IComparisonSorting<T> where T : IComparable<T>
    {
        public void Sort(T[] arr)
        {
            Sort(arr, 0, arr.Length-1);
        }

        private void Sort(T[] arr, int left, int right) 
        {
            if(left >= right)
                return;
            
            //pick a pivot
            //parition arr according to the pivot
            //recursively sort the 2 partitions
            int q = Partition(arr, left, right);
            Sort(arr, left, q-1);
            Sort(arr, q+1, right);
        }

        private int Partition(T[] arr, int left, int right) 
        {   
            var pivot = arr[right];
            int q = left;
            //[less_piv, greateq_piv] q is the first of greateq_piv
            for(int i = left; i <= right; ++i) {
                if(arr[i].CompareTo(pivot) < 0) {
                    (arr[q], arr[i]) = (arr[i], arr[q]);
                    q++;
                }
            }
            (arr[q], arr[right]) = (arr[right], arr[q]);
            return q;
        }

    }
}
