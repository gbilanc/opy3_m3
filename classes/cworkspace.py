# encoding: utf-8

"""
Module for managing the plotter workspace.

This module provides the functionality to load DXF files, extract layers, 
and perform global geometric transformations (translation, rotation, flipping) 
across the entire workspace.
"""

from ezdxf import readfile
from ezdxf.groupby import groupby

from .clayer import CLayer


def get_layers(dxf):
    """
    Extracts layers from a DXF document and translates them to a local coordinate system.

    Args:
        dxf: An ezdxf document object.

    Returns:
        list: A list of CLayer objects containing the parsed entities and metadata 
              from the DXF file, normalized based on the document's minimum extent.
    """
    ext_min = dxf.header['$EXTMIN']
    msp = dxf.modelspace()
    layer_list = list()
    group = groupby(entities=msp, dxfattrib="layer")
    for layer_name, values in group.items():
        layer = CLayer(dxf.layers.get(layer_name), values)
        layer.translate(-ext_min[0], -ext_min[1])
        layer_list.append(layer)
    return layer_list


class CWorkspace(object):
    """
    Represents the global drawing workspace for the plotter.

    The CWorkspace class orchestrates the management of multiple layers, 
    handles the selection of specific layers, and provides high-level methods 
    to transform the entire set of drawing entities.

    Attributes:
        layers (list): List of CLayer objects present in the workspace.
        colors (list): A unique set of all colors used across all layers.
        selected_layer (CLayer): The currently selected layer, or None if no selection.
    """

    def __init__(self, dxf_file):
        """
        Initializes the workspace by loading a DXF file.

        Args:
            dxf_file (str): Path to the DXF file to be loaded.
        """
        dxf = readfile(dxf_file)
        self.layers = get_layers(dxf)
        self.colors = self.__get_colors()
        self.selected_layer = None

    def __get_colors(self):
        """
        Gathers all unique colors used across all layers in the workspace.

        Returns:
            list: A list of unique color identifiers.
        """
        color_list = [[color for color in layer.colors] for layer in self.layers]
        color_list = [inner for outer in color_list for inner in outer]
        return list(set(color_list))

    def layer_with_name(self, name):
        """
        Retrieves a layer object based on its name.

        Args:
            name (str): The name of the layer to search for.

        Returns:
            CLayer: The layer object if found, otherwise None.
        """
        list_names = [item for item in self.layers if item.name == name]
        return list_names[0] if list_names else None

    @property
    def bounds(self):
        """
        Returns the bounding box of the workspace.
        
        Note: Currently relies on the bounds of the layer named "1".

        Returns:
            tuple: The bounding box coordinates.
        """
        return self.layer_with_name("1").bounds

    @property
    def center(self):
        """
        Calculates the center point of the workspace.
        
        Note: Currently relies on the center of the layer named "1".

        Returns:
            tuple: The (x, y) coordinates of the center.
        """
        return self.layer_with_name("1").center

    def translate(self, off_x, off_y):
        """
        Translates all layers in the workspace by a given offset.

        Args:
            off_x (float): Offset along the X axis.
            off_y (float): Offset along the Y axis.
        """
        bounds = self.bounds
        for item in self.layers:
            item.translate(off_x - bounds[0], off_y - bounds[1])

    def rotate(self, radians):
        """
        Rotates all layers around the workspace center.

        Args:
            radians (float): Rotation angle in radians.
        """
        center = self.center
        for item in self.layers:
            item.rotate(radians, center)

    def flip(self, mode):
        """
        Flips all layers across the workspace center based on the specified mode.

        Args:
            mode (int/str): The flip axis or mode (e.g., horizontal or vertical).
        """
        center = self.center
        for item in self.layers:
            item.flip(mode, center)

    def select_layer_with_name(self, layer_name):
        """
        Sets a specific layer as selected and deselects all others.

        Args:
            layer_name (str): The name of the layer to select.

        Returns:
            CLayer: The newly selected layer object.
        """
        for item in self.layers:
            if item.name == layer_name:
                item.do_selected(True)
                self.selected_layer = item
            else:
                item.do_selected(False)
        return self.selected_layer
