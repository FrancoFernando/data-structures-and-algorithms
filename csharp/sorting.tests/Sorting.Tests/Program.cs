namespace Algorithms.Sorting.Tests
{
    public class Program
    {
        private const int n = 15;
        private static int[] arr = new int[n];
        private static (int key, string val)[] intArr = new (int key, string val)[n];

        public static void Main()
        {
            RunIntegerAlgorithm(new CountingSort<string>());
            RunAlgorithm(new SelectionSort<int>());
            RunAlgorithm(new MergeSort<int>());
        }

        private static void RunIntegerAlgorithm(IIntegerSorting<string> algo)
        {
            SortingHelper.FillArray(intArr);
            Console.WriteLine("Unsorted array:");
            SortingHelper.PrintArray(intArr);
            Console.WriteLine("Run Algorithm:");
            intArr = algo.Sort(intArr);
            Console.WriteLine("Sorted array:");
            SortingHelper.PrintArray(intArr);
        }

        private static void RunAlgorithm(IComparisonSorting<int> algo)
        {
            SortingHelper.FillArray(arr);
            Console.WriteLine("Unsorted array:");
            SortingHelper.PrintArray(arr);
            Console.WriteLine("Run Algorithm:");
            algo.Sort(arr);
            Console.WriteLine("Sorted array:");
            SortingHelper.PrintArray(arr);
        }
    }
}
