using System;
using System.Collections.Generic;
using System.Linq;

namespace Algorithms
{
    class Program {

        public int CountDigits(int num) {
			return (int)Math.Floor(Math.Log10(num)+1);
		}
		
		private int[] PartialSum(int[] input)
		{
				for (int i = 1; i < input.Length; i++)
				{
						input[i] = input[i] + input[i-1];
				}

				return input;
		}
		
		public List<int> CountingSort(List<int> input, int digit_position) {
			
			int[] bookkeeping = new int[10];
			
			int digit_column = (int)Math.Pow(10, digit_position);
			
			foreach(int num in input) {
				int digit = (num / digit_column) % 10;
				bookkeeping[digit]++;
			}
			
			bookkeeping = PartialSum(bookkeeping);
			
			var output = new List<int>(new int[input.Count()]);
			
			for (int i = input.Count()-1; i >= 0; --i) {
				int digit = (input[i] / digit_column) % 10;
				output[--bookkeeping[digit]] = input[i];
			}
			
			return output;
		} 

		public List<int> RadixSort(List<int> input) {
			
			if (!input.Any()) return input;
			
			//Find the maximum element
			int max_number = input.Max();
			int digits = CountDigits(max_number);
			
			for (int digit = 0; digit < digits; ++digit) {
				input = CountingSort(input, digit);
			}
			
			return input;
		}
		
		static void Main(string[] args)
        {
            Console.WriteLine("Radix Sort Test");
 
            var input = new int[] { 8762, 654, 3008, 345, 87, 65, 234, 12, 2 };
            
            Console.WriteLine("Input");
			string text = "";
            foreach (var num in input) {
                text += num + " ";
            }
			Console.WriteLine(text);
            
            var output = RadixSort(input);

            text = "";
            foreach (var num in output) {
                text += num + " ";
            }
			Console.WriteLine(text);
        }
    }
}