using System;
using System.Collections.Generic;
using System.Linq;

namespace Algorithms
{
    class CountingSort {

        private static int[] PartialSum(int[] input)
        {
            for (int i = 1; i < input.Count(); i++)
            {
                input[i] = input[i] + input[i - 1];
            }

            return input;
        }

        public static (int, string)[] CountingSort((int, string)[] items)
        {
            int max_key = items.Max(t => t.Item1);
            var bookkeeping = new int[max_key + 1];

            //count keys frequency
            foreach (var item in items) {
                bookkeeping[item.Item1]++;
            }

            //at the end each element is the index of the last element with that key
            bookkeeping = PartialSum(bookkeeping);

            var output = new (int, string)[items.Length];

            //build sorted output iterating backward
            for (int i = items.Length - 1; i >= 0; i--) {
                output[--bookkeeping[items[i].Item1]] = items[i];
            }

            return output;
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Counting Sort Test");
 
            var input = new (int, string)[] { (1, "a"), (1, "b"), (2, "c"), (4, "d"), (3, "e"), (0, "f"), (1, "g"), (2, "h"), (3, "i"), (1, "l") };
            
            Console.WriteLine("Input");
            foreach (var item in output) {
                Console.WriteLine("(" << item.Item1 << ", " << item.Item2 << ")");
            }
            
            var output = CountingSort(input);

            Console.WriteLine("Output");
            foreach (var item in output) {
                Console.WriteLine("(" << item.Item1 << ", " << item.Item2 << ")");
            }
        }
    }
}