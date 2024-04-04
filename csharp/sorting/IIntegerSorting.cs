namespace Sorting
{
    public interface IIntegerSorting<T>
    {
        (int key, T val)[] Sort((int key, T val)[] array);
    }
}
