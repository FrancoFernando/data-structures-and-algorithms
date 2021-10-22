using System;
using System.Collections.Generic;
using System.Linq;

namespace Algorithms
{
    class BubbleSort {

        public static int[] BubbleSort(int[] input)
        {
            bool has_swapped = true;
            int iterations = 0, length = input.Length;

            while (has_swapped)
            {
                has_swapped = false;
                for (int i = 0; i < length-iterations-1; ++i)
                {
                    if (input[i] > input[i+1])
                    {
                        (input[i], input[i+1]) = (input[i+1], input[i]);
                        has_swapped = true;
                    }
                }
                iterations++;
            }
            return input;
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Bubble Sort Test");
 
            var input = new int[] {2,5,1,2,4};
            
            Console.WriteLine("Input");
            foreach (var num in input) {
                Console.WriteLine(num);
            }
            
            var output = CountingSort(input);

            Console.WriteLine("Output");
            foreach (var num in output) {
                Console.WriteLine(num);
            }
        }
    }
}