namespace Sorting
{
    public static class IntegerSortingHelper
    {
        private static Random generator = new Random(-1);
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

        public static void PrintArray((int key, string val)[] arr)
        {
            foreach (var item in arr)
            {
                Console.WriteLine(item.key + " " + item.val);
            }
        }
    }
}
