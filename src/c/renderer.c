#include <Python.h>

static PyObject* render(PyObject* self, PyObject* args) {
    const char* text;
    if (!PyArg_ParseTuple(args, "s", &text)) {
        return NULL;
    }
    // Rendering logic here
    printf("Rendering: %s\n", text);
    Py_RETURN_NONE;
}

static PyMethodDef RendererMethods[] = {
    {"render", render, METH_VARARGS, "Render text"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef renderermodule = {
    PyModuleDef_HEAD_INIT,
    "renderer",
    NULL,
    -1,
    RendererMethods
};

PyMODINIT_FUNC PyInit_renderer(void) {
    return PyModule_Create(&renderermodule);
}