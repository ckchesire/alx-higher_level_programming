#include <Python.h>
#include <object.h>
#include <unicodeobject.h>

/**
 * print_python_string - Function that prints Python strings
 * @p: pointer to python object expected to be string
 */
void print_python_string(PyObject *p)
{
	const char *type = NULL;
	Py_ssize_t length = 0;
	wchar_t *str = NULL;

	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(p))
		type = "compact ascii";
	else
		type = "compact unicode object";

	str = PyUnicode_AsWideCharString(p, &length);
	if (str != NULL)
	{
		printf("  type: %s\n", type);
		printf("  length: %ld\n", length);
		printf("  value: %ls\n", str);
		PyMem_Free(str);
	}
}
