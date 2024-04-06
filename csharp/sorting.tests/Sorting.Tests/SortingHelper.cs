namespace Algorithms.Sorting.Tests
{
    public static class SortingHelper
    {
        private static Random generator = new Random();
        private const string chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
        public static void FillArray((int key, string val)[] arr)
        {
            for (var i = 0; i < arr.Length; i++)
            {
                var stringChars = new char[8];
                
                for (int j = 0; j < stringChars.Length; j++)
                {
                    stringChars[j] = chars[generator.Next(chars.Length)];
                }
                arr[i] = (generator.Next(1000), new String(stringChars));
            }
        }

        public static void FillArray(int[] arr)
        {
            for (var i = 0; i < arr.Length; i++)
            {
                arr[i] = generator.Next(-1_000, 1_000);
            }
        }

        public static void PrintArray(int[] arr)
        {
            foreach (var item in arr)
            {
                Console.WriteLine(item + " ");
            }
        }

        public static void PrintArray((int key, string val)[] arr)
        {
            foreach (var item in arr)
            {
                Console.WriteLine(item.key + " " + item.val);
            }
        }
    }
}
