#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Displays fundamental details regarding Python lists.
 * @p: An input PyObject representing a list.
 */
void print_python_list(PyObject *p)
{
	int size, i;
	PyListObject *list;
	const char *type;

	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}
	list = (PyListObject *)p;
	size = Py_SIZE(list);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %ld\n", (long)list->allocated);

	for (i = 0; i < size; i++)
	{
		type = Py_TYPE(list->ob_item[i])->tp_name;
		printf("Element %d: %s\n", i, type);

		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - Presents essential information
 * about Python byte objects.
 * @p: A PyObject representing a byte object.
 */
void print_python_bytes(PyObject *p)
{
	unsigned char i, size;
	PyBytesObject *bytes;

	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = (PyBytesObject *)p;
	size = Py_SIZE(bytes);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", (long)size);
	printf("  trying string: %s\n", bytes->ob_sval);

	size = (size > 10) ? 10 : size;
	printf("  first %d bytes: ", size);

	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
