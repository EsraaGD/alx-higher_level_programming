#define PY_SSIZE_T_CLEAN
#include "lists.h"
#include <Python.h>

void print_python_list_info(PyObject *p) {
    int size, alloc;
    PyListObject *list = (PyListObject *)p;
    PyObject *element;

    size = Py_SIZE(p);
    alloc = list->allocated;

    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", alloc);

    for (int i = 0; i < size; i++) {
        element = PyList_GetItem(p, i);
        printf("Element %d: %s\n", i, Py_TYPE(element)->tp_name);
    }
}
