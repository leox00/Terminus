#include <Python.h>
#include <pty.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

static PyObject* start_pty(PyObject* self, PyObject* args) {
    int master_fd, slave_fd;
    pid_t pid;

    if (openpty(&master_fd, &slave_fd, NULL, NULL, NULL) == -1) {
        perror("openpty");
        return NULL;
    }

    pid = fork();
    if (pid == -1) {
        perror("fork");
        return NULL;
    } else if (pid == 0) {
        close(master_fd);
        login_tty(slave_fd);
        execlp("bash", "bash", NULL);
        perror("execlp");
        exit(EXIT_FAILURE);
    } else {
        close(slave_fd);
        return Py_BuildValue("i", master_fd);
    }
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