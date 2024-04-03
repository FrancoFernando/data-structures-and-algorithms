using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Algorithms.Sorting.Tests
{
    [TestClass]
    public class SelectionSortTest
    {
        private const int n = 10;
        private int[] testArr = new int[n];
        private int[] correctArray = new int[n];
        public void Initialize()
        {
            var generator = new Random(-1);
            for (var i = 0; i < n; i++)
            {
                var t = generator.Next(-1_000, 1_000);
                testArr[i] = t;
                correctArray[i] = t;
            }
        }

        [TestMethod]
        public void IntegerArrayTest()
        {
            var sortingAlgorithm = new SelectionSort<int>();
            sortingAlgorithm.Sort(testArr);
            Array.Sort(correctArray);
            CollectionAssert.AreEqual(testArr, correctArray);
        }
    }
}

