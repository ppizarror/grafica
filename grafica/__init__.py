"""
Grafica library.
"""

import platform as __platform

# patch glfw for MACOS
if __platform.system() == 'Darwin':
    import glfw as __glfw


    def __create_window(width, height, title, monitor, share):
        """
        Creates a window and its associated context.

        Wrapper for:
            GLFWwindow* glfwCreateWindow(int width, int height, const char* title, GLFWmonitor* monitor, GLFWwindow* share);
        """
        __glfw.window_hint(__glfw.CONTEXT_VERSION_MAJOR, 3)
        __glfw.window_hint(__glfw.CONTEXT_VERSION_MINOR, 3)
        __glfw.window_hint(__glfw.OPENGL_FORWARD_COMPAT, True)
        __glfw.window_hint(__glfw.OPENGL_PROFILE, __glfw.OPENGL_CORE_PROFILE)
        # noinspection PyProtectedMember
        return __glfw._glfw.glfwCreateWindow(width, height, __glfw._to_char_p(title),
                                             monitor, share)


    __glfw.create_window = __create_window
