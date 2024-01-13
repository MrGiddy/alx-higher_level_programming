#include <Python.h>

/**
 * print_python_list_info - Prints some basic info about Python lists
 * @p: A Python list object
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	int i;

	list = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < PyList_Size(p); i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);

		/* printf("Element %d: %s\n", i, list->ob_item[i]->ob_type->tp_name); */
	}
}
