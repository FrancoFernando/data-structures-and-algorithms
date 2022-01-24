using System;

namespace Algorithms.Sorters
{
    class SelectionSorter
    {
        public static T[] Sort<T>(T[] input) where T : IComparable<T>
        {
            for (int i = 0; i < input.Length - 1; ++i)
            {
                int smallest_index = i;

                for (int j = i + 1; j < input.Length; ++j)
                {
                    if (input[j].CompareTo(input[smallest_index]) < 0)
                    {
                        smallest_index = j;
                    }
                }
                (input[i], input[smallest_index]) = (input[smallest_index], input[i]);
            }
            return input;
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Selection Sort Test");

            var input = new int[] { 2, 5, 1, 3, 4 };

            Console.WriteLine("Input");
            foreach (var num in input)
            {
                Console.WriteLine(num);
            }

            var output = Sort<int>(input);

            Console.WriteLine("Output");
            foreach (var num in output)
            {
                Console.WriteLine(num);
            }
        }
    }
}