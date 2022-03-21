# coding=utf-8
"""
Provide glfw utils.
"""

__all__ = ['create_window']

__author__ = "Pablo Pizarro R."
__license__ = "MIT"

import platform

if platform.system() == 'Darwin':
    # noinspection PyProtectedMember
    from glfw import window_hint, CONTEXT_VERSION_MAJOR, CONTEXT_VERSION_MINOR, \
        OPENGL_FORWARD_COMPAT, OPENGL_PROFILE, OPENGL_CORE_PROFILE, _glfw, _to_char_p


    def create_window(width, height, title, monitor, share):
        """
        Creates a window and its associated context.

        Wrapper for:
            GLFWwindow* glfwCreateWindow(int width, int height, const char* title, GLFWmonitor* monitor, GLFWwindow* share);
        """
        window_hint(CONTEXT_VERSION_MAJOR, 3)
        window_hint(CONTEXT_VERSION_MINOR, 3)
        window_hint(OPENGL_FORWARD_COMPAT, True)
        window_hint(OPENGL_PROFILE, OPENGL_CORE_PROFILE)
        return _glfw.glfwCreateWindow(width, height, _to_char_p(title),
                                      monitor, share)
else:
    from glfw import create_window
