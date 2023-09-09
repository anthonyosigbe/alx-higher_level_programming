#include <Python.h>

/**
* print_python_list_info - Display fundamental information about Python lists.
* @p: A list of PyObject objects.
*/
void print_python_list_info(PyObject *p)
{
	int range, alloc, index;
	PyObject *obj;

	range = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", range);
	printf("[*] Allocated = %d\n", alloc);

	for (index = 0; index < range; index++)
	{
		printf("Element %d: ", index);
		obj = PyList_GetItem(p, index);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
