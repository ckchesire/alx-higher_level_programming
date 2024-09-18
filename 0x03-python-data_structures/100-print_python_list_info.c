#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - prints basic info about python lists
 * @p: python list
 * Return: return nothing
 */
void print_python_list_info(PyObject *p)
{
	int ctype;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (ctype = 0; ctype < Py_SIZE(p); ctype++)
		printf("Element %d: %s\n", ctype, Py_TYPE(PyList_GetItem(p, ctype))->tp_name);
}
