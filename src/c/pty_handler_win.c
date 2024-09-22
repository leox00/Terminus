#include <Python.h>
#include <windows.h>
#include "winpty.h"

static PyObject* start_pty(PyObject* self, PyObject* args) {
    winpty_t* wp;
    winpty_spawn_config_t* config;
    winpty_error_ptr_t err;
    HANDLE process_handle, thread_handle;
    DWORD create_process_error;
    const wchar_t* cmdline = L"cmd.exe";

    wp = winpty_open(0, &err);
    if (wp == NULL) {
        return NULL;
    }

    config = winpty_spawn_config_new(WINPTY_SPAWN_FLAG_AUTO_SHUTDOWN, cmdline, NULL, NULL, NULL, &err);
    if (config == NULL) {
        winpty_free(wp);
        return NULL;
    }

    if (!winpty_spawn(wp, config, &process_handle, &thread_handle, &create_process_error, &err)) {
        winpty_spawn_config_free(config);
        winpty_free(wp);
        return NULL;
    }

    winpty_spawn_config_free(config);
    return Py_BuildValue("i", (int)process_handle);
}

static PyMethodDef PtyMethods[] = {
    {"start_pty", start_pty, METH_VARARGS, "Start a PTY"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef ptymodule = {
    PyModuleDef_HEAD_INIT,
    "pty_handler",
    NULL,
    -1,
    PtyMethods
};

PyMODINIT_FUNC PyInit_pty_handler(void) {
    return PyModule_Create(&ptymodule);
}