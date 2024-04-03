using Algorithms.Sorting;

namespace Sorting
{
    public class Program
    {
        private const int n = 15;
        private static int[] arr = new int[n];
        private static Random generator = new Random(-1);

        public static void Main()
        {
            RunAlgorithm(new SelectionSort<int>());
            RunAlgorithm(new MergeSort<int>());
        }

        private static void RunAlgorithm(ISortingAlgorithm<int> algo)
        {
            FillArray();
            Console.WriteLine("Unsorted array:");
            PrintArray();
            Console.WriteLine("Run Algorithm:");
            algo.Sort(arr);
            Console.WriteLine("Sorted array:");
            PrintArray();
        }

        private static void PrintArray()
        {
            foreach (var item in arr)
            {
                Console.WriteLine(item + " ");
            }
        }

        private static void FillArray()
        {
            for (var i = 0; i < n; i++)
            {
                arr[i] = generator.Next(-1_000, 1_000);
            }
        }
    }
}
