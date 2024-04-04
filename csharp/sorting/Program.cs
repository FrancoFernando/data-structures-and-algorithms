using System.Xml;
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
            RunIntegerAlgorithm(new CountingSort<string>());
            RunAlgorithm(new SelectionSort<int>());
            RunAlgorithm(new MergeSort<int>());
        }

        private static void RunIntegerAlgorithm(IIntegerSorting<string> algo)
        {
            (int key, string val)[] intArr = {(5,"one"), (3,"two"), (4,"three"), (5,"four"), (5,"five")};
            Console.WriteLine("Unsorted array:");
            foreach (var item in intArr)
            {
                Console.WriteLine(item.key + " " + item.val);
            }
            Console.WriteLine("Run Algorithm:");
            var output = algo.Sort(intArr);
            Console.WriteLine("Sorted array:");
            foreach (var item in output)
            {
                Console.WriteLine(item.key + " " + item.val);
            }
        }

        private static void RunAlgorithm(IComparisonSorting<int> algo)
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

        private static void PrintIntArray()
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
