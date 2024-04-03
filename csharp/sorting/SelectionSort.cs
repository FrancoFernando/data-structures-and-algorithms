using Sorting;

namespace Algorithms.Sorting
{
    public class SelectionSort<T> : ISortingAlgorithm<T> where T : IComparable<T>
    {
        public void Sort(T[] arr)
        {
            for (int i = 0; i < arr.Length - 1; i++)
            {
                int minIndex = i;
                for (int j = i + 1; j < arr.Length; j++)
                {
                    if (arr[j].CompareTo(arr[minIndex]) < 0)
                    {
                        minIndex = j;
                    }
                }
                
                (arr[i], arr[minIndex]) = (arr[minIndex], arr[i]);
            }
        }
    }
}
