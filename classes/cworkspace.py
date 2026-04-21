# encoding: utf-8

from ezdxf import readfile
from ezdxf.groupby import groupby

from .clayer import CLayer


def get_layers(dxf):
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

    def __init__(self, dxf_file):
        dxf = readfile(dxf_file)
        self.layers = get_layers(dxf)
        self.colors = self.__get_colors()
        self.selected_layer = None

    def __get_colors(self):
        color_list = [[color for color in layer.colors] for layer in self.layers]
        color_list = [inner for outer in color_list for inner in outer]
        return list(set(color_list))

    def layer_with_name(self, name):
        list_names = [item for item in self.layers if item.name == name]
        return list_names[0] if list_names else None

    @property
    def bounds(self):
        return self.layer_with_name("1").bounds

    @property
    def center(self):
        return self.layer_with_name("1").center

    def translate(self, off_x, off_y):
        bounds = self.bounds
        for item in self.layers:
            item.translate(off_x - bounds[0], off_y - bounds[1])

    def rotate(self, radians):
        center = self.center
        for item in self.layers:
            item.rotate(radians, center)

    def flip(self, mode):
        center = self.center
        for item in self.layers:
            item.flip(mode, center)

    def select_layer_with_name(self, layer_name):
        for item in self.layers:
            if item.name == layer_name:
                item.do_selected(True)
                self.selected_layer = item
            else:
                item.do_selected(False)
        return self.selected_layer
