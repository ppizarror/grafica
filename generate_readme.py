# coding=utf-8
"""Generate a nice and pretty Readme.md file for the repository"""

import os.path
import ast

__author__ = "Daniel Calderon"
__license__ = "MIT"


def getDocString(filepath):
    with open(filepath) as f:
        return ast.get_docstring(ast.parse(f.read()))
    return None


if __name__ == "__main__":

    examplesPath = "examples"

    headerText = """
# Computer Graphics with OpenGL and Python

This set of examples illustrate different computer graphics concepts in 2D and 3D while using: Python, OpenGL core profile, GLFW and Numpy.
    """

    ExampleFamilyTemplateText = """
## $EXAMPLE_FAMILY_FILENAME$

    """

    ExampleTemplateText = """
### $EXAMPLE_FILENAME$
$DESCRIPTION$
    """

    ExampleImageTemplateText = """
[![$EXAMPLE_FILENAME$](./screenshots/$SCREENSHOT_FILENAME$)](./examples/$EXAMPLE_FILENAME$)
    """

    dirPath = os.path.dirname(os.path.realpath(__file__))
    screenshotsDir = os.path.join(dirPath, "screenshots")
    readmeFilename = os.path.join(dirPath, "Readme.md")


    # print("this path: ", dir_path)

    class ExampleFamily:
        def __init__(self, category, examples):
            self.category = category
            self.examples = examples


    exampleList = [
        ExampleFamily("Raster", [
            "ex_color_palette.py",
            "ex_color_palette_anim.py",
            "ex_sira_direct.py",
            "ex_sira_indirect.py"]),
        ExampleFamily("OpenGL Basics", [
            "opengl_version.py",
            "ex_triangle.py",
            "ex_quad.py",
            "ex_cube.py",
            "ex_stream_draw.py"]),
        ExampleFamily("Transformations", [
            "ex_transform_polygon.py",
            "ex_cpu_transforms.py",
            "ex_4shapes.py",
            "ex_transformations_showcase.py",
            "ex_quad_controlled.py",
            "ex_transform_imgui.py",
            "ex_mouse.py"]),
        ExampleFamily("Textures", [
            "ex_texture_boo.py",
            "ex_texture_quad.py",
            "ex_mipmap.py",
            "ex_binding_textures.py",
            "ex_text_renderer.py"]),
        ExampleFamily("Scene Graphs", [
            "ex_scene_graph_2dcars.py",
            "ex_scene_graph_snowman.py"]),
        ExampleFamily("Curves", [
            "ex_curves.py"]),
        ExampleFamily("3D World", [
            "ex_projections.py",
            "ex_texture_dice.py",
            "ex_height_plotter.py",
            "ex_scene_graph_3dcars.py",
            "ex_mix2d3d.py",
            "ex_surface.py",
        ]),
        ExampleFamily("Shading and Lighting", [
            "ex_lighting.py",
            "ex_lighting_texture2.py",
            "ex_obj_reader.py",
        ]),
        ExampleFamily("Meshes", [
            "ex_delaunay.py",
            "ex_triangle_mesh.py",
            "ex_triangle_mesh_builder.py",
            "ex_openmesh_pyramid.py"
        ]),
        ExampleFamily("Physics and Collisions", [
            "ex_collisions.py",
        ]),
        ExampleFamily("Advanced OpenGL", [
            "ex_geometry_shader.py",
            "ex_render_to_texture.py"
        ])
        # ExampleFamily("Volumetric Rendering",[
        #    "ex4_mayavi.py"
        # ])
    ]

    with open(readmeFilename, 'w') as f:

        f.write(headerText)

        for exampleFamily in exampleList:
            print("Processing Category: ", exampleFamily.category)
            f.write(ExampleFamilyTemplateText.replace("$EXAMPLE_FAMILY_FILENAME$", exampleFamily.category))

            for filename in exampleFamily.examples:
                print("    Procesing example: ", filename)  # , filename.__doc__)

                filepath = os.path.join(examplesPath, filename)

                description = ""
                if os.path.isfile(filepath):
                    description = getDocString(filepath)

                f.write(ExampleTemplateText \
                        .replace("$EXAMPLE_FILENAME$", filename) \
                        .replace("$DESCRIPTION$", description))

                pngScreenshotCandidate = os.path.join(screenshotsDir, filename[:-3] + ".png")
                hasPngScreenshot = os.path.isfile(pngScreenshotCandidate)

                gifScreenshotCandidate = os.path.join(screenshotsDir, filename[:-3] + ".gif")
                hasGifScreenshot = os.path.isfile(gifScreenshotCandidate)

                if hasPngScreenshot:
                    f.write(ExampleImageTemplateText \
                            .replace("$EXAMPLE_FILENAME$", filename) \
                            .replace("$SCREENSHOT_FILENAME$", filename[:-3] + ".png"))
                elif hasGifScreenshot:
                    f.write(ExampleImageTemplateText \
                            .replace("$EXAMPLE_FILENAME$", filename) \
                            .replace("$SCREENSHOT_FILENAME$", filename[:-3] + ".gif"))

                # print(filename)
                # print(hasPngScreenshot, hasGifScreenshot)
                # print()
