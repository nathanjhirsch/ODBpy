import re

class Component:
    def __init__(self, pkg_ref, x, y, rot, mirror, comp_name, part_name, properties=None):
        self.pkg_ref = pkg_ref
        self.x = float(x)
        self.y = float(y)
        self.rot = float(rot)
        self.mirror = mirror
        self.comp_name = comp_name
        self.part_name = part_name
        self.properties = properties if properties is not None else []

    def __repr__(self):
            return f"CMP {self.pkg_ref} {self.x} {self.y} {self.rot} {self.mirror} {self.comp_name} {self.part_name}"

class Property:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
            return f"PRP {self.name} {self.value}"

def parse_file(filename):
    components = []
    with open(filename) as f:
        component = None
        for line in f:
            line = line.strip()
            if line.startswith('CMP'):
                if component is not None:
                    components.append(component)
                pkg_ref, x, y, rot, mirror, comp_name, part_name = parse_cmp_line(line)
                component = Component(pkg_ref, x, y, rot, mirror, comp_name, part_name)
            elif line.startswith('PRP'):
                if component is None:
                    raise ValueError('Invalid file format')
                prop = parse_property_line(line)
                component.properties.append(prop)
        if component is not None:
            components.append(component)
    return components

def parse_cmp_line(line):
    parts = line.split(';')
    header_parts = parts[0].split()
    pkg_ref, x, y, rot, mirror, comp_name, part_name = header_parts[1:8]
    attributes_str = parts[1].strip() if len(parts) > 1 else ''
    return pkg_ref, x, y, rot, mirror, comp_name, part_name

def parse_property_line(line):
    parts = line.split()
    prop = Property(parts[1], parts[2].strip("'"))
    return prop

file_path = r'C:\Users\hirsc\Desktop\odbPY\ODB_test_files\max14883e_evkit_a_odb_v7\steps\stp\layers\comp_+_top\components'
listofcomps = parse_file(file_path)

for comp in listofcomps:
    print(comp.properties)