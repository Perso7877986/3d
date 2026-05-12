import cadquery as cq
from cadquery import exporters

# Dimensions en MILLIMÈTRES
outer_diameter = 39.0
inner_diameter = 28.0
height = 15.0

# Tube
part = (
    cq.Workplane("XY")
    .circle(outer_diameter / 2)
    .circle(inner_diameter / 2)
    .extrude(height)
)

# Export STL
exporters.export(part, "tube_39mm.stl")

print("STL créé avec dimensions correctes.")