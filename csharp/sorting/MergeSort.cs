using System.ComponentModel.DataAnnotations;
using Sorting;

namespace Algorithms.Sorting
{
    public class MergeSort<T> : IComparisonSorting<T> where T : IComparable<T>
    {
        public void Sort(T[] arr)
        {
            MergeSortAlgo(arr, 0, arr.Length-1);
        }

        private void MergeSortAlgo(T[] arr, int left, int right) 
        {
            if(left == right)
                return;
            
            int m = (int)((left + right) / 2);
            MergeSortAlgo(arr, left, m);
            MergeSortAlgo(arr, m+1, right);
            Merge(arr, left, right);
        }

        private void Merge(T[] arr, int left, int right) 
        {
            T[] tmp = new T[right-left+1];
            int m = (left + right) / 2;
            int w = 0, i = left, j = m+1;
            while (i <= m && j <= right) 
            {
                if(arr[i].CompareTo(arr[j]) < 0) 
                    tmp[w++] = arr[i++];
                else
                    tmp[w++] = arr[j++];
            }
            
            while (i <= m) tmp[w++] = arr[i++];
            while (j <= right) tmp[w++] = arr[j++];
            tmp.CopyTo(arr, left);
        }

    }
}
