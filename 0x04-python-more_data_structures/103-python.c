#include <Python.h>
#include <stdio.h>

/* Function to print basic info about Python lists */
void print_python_list(PyObject *p) {
	if (PyList_Check(p)) {
		Py_ssize_t size = PyList_Size(p);
		Py_ssize_t i;

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

		for (i = 0; i < size; i++) {
			PyObject *item = PyList_GetItem(p, i);
			const char *typeName = Py_TYPE(item)->tp_name;
			printf("Element %ld: %s\n", i, typeName);
		}
	} else {
		printf("  [ERROR] Invalid List Object\n");
	}
}

/* Function to print basic info about Python bytes */
void print_python_bytes(PyObject *p) {
	if (PyBytes_Check(p)) {
		Py_ssize_t size = PyBytes_Size(p);
		Py_ssize_t i;

		printf("[.] bytes object info\n");
		printf("  [ERROR] Bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
		printf("[*] Size: %ld\n", size);
		printf("[*] trying string: %s\n", PyBytes_AsString(p));
		printf("[*] first 10 bytes: ");

		if (size > 10) {
			size = 10;
		}

		for (i = 0; i < size; i++) {
			printf("%02x", (unsigned char)PyBytes_AS_STRING(p)[i]);
			if (i < size - 1) {
				printf(" ");
			}
		}

		printf("\n");
	} else {
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}

int main(int argc, char **argv) {
	(void)argc;
	(void)argv;

	/* Initialize the Python interpreter */
	Py_Initialize();

	/* Create and print a Python list */
	PyObject *list = PyList_New(0);
	print_python_list(list);

	/* Create and print a Python bytes object */
	const char *bytes_data = "Hello, Python!";
	PyObject *bytes = PyBytes_FromStringAndSize(bytes_data, strlen(bytes_data));
	print_python_bytes(bytes);

	/* Finalize the Python interpreter */
	Py_Finalize();

	return (0);
}
