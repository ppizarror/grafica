|
Instalación de python y librerias en OS X
=======

Instalación de Brew
---------------------

Primero hay que revisar si ``brew`` esta instalado, para esto abra su terminal

Ejecute ``brew``. Si la respuesta es algo de este tipo:

    Example usage:
      brew search TEXT|/REGEX/
      brew info [FORMULA|CASK...]
      brew install FORMULA|CASK...
      brew update
      brew upgrade [FORMULA|CASK...]
      brew uninstall FORMULA|CASK...
      brew list [FORMULA|CASK...]

    Troubleshooting:
      brew config
      brew doctor
      brew install --verbose --debug FORMULA|CASK

    Contributing:
      brew create URL [--no-fetch]
      brew edit [FORMULA|CASK...]

    Further help:
      brew commands
      brew help [COMMAND]
      man brew
      https://docs.brew.sh

Entonces ``brew`` esta instalado.

En caso de no estar instalado Para instalar ``brew`` se pueden seguir las instrucciones en [https://brew.sh](https://brew.sh).

Instalación de python3
----------------------

En la terminal ejecute:

    brew install --cask miniforge
    conda init zsh

Se le pedirá su contraseña de sistema, ingrésela y luego ingrese 'y' o 's' para comenzar la instalación.

Creando un environment
----------------------

Existen múltiples librerías para python. Algunas incompatibles entre si debido a distintos requerimientos de versiones. Es posible crear distintos ambientes de trabajo para tener ejecutables de python con distintas librerías específicas según sea el caso. Se recomienda instalar todas las librerías para el curso en un environment dedicado. Así no interfiere con pythons que pueda utilizar para otros fines.

Para crear un entorno con conda ejecute lo siguiente en la terminal:

    conda create --name grafica python=3.9

Esto creará el entorno "grafica" disponible en todo el sistema. Puede renombrar a cualquier otro, excepto "base".

Instalando librerías
--------------------

Primero active su nuevo entorno

    conda activate grafica

Aparecerá (grafica) al lado izquierdo de su prompt, indicando que dicho environment se encuentra activo.

Puede probar que la versión de python activa es la que se encuentra en su environment con

    which python

La respuesta debiera ser

    /opt/homebrew/Caskroom/miniforge/base/envs/grafica/bin/python

Instalemos algunas dependencias necesarias:

    brew install glfw

Ahora instalamos todas las librerias python requeridas

    python -m pip install numpy scipy matplotlib ipython jupyter pyopengl glfw pillow openmesh imgui open3d

Siempre es posible instalar cada librería por separado.

Arreglar glfw
-------------

Para que todos los programas corran correctamente debera agregar el siguiente bloque de codigo en la linea 1180

    [ 1174 ] """
    [ 1175 ] Creates a window and its associated context.
    [ 1176 ]
    [ 1177 ] Wrapper for:
    [ 1178 ]     GLFWwindow* glfwCreateWindow(int width, int height, const char* title, GLFWmonitor* monitor, GLFWwindow* share);
    [ 1179 ] """
    # Agregar esto:
    [ 1180 ] window_hint(CONTEXT_VERSION_MAJOR, 3)
    [ 1181 ] window_hint(CONTEXT_VERSION_MINOR, 3)
    [ 1182 ] window_hint(OPENGL_FORWARD_COMPAT, True)
    [ 1183 ] window_hint(OPENGL_PROFILE, OPENGL_CORE_PROFILE)

al archivo ~/pythoncg/lib/python3.9/site-packages/glfw/\_\_init\_\_.py
