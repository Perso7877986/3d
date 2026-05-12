import cadquery as cq
from cadquery import exporters

# Dimensions converties en mm
outer_diameter = 39.0   # 3.9 cm
inner_diameter = 28.0   # 2.8 cm
height = 15.0           # 1.5 cm

# Création du tube
part = (
    cq.Workplane("XY")
    .circle(outer_diameter / 2)
    .circle(inner_diameter / 2)
    .extrude(height)
)

# Export STL
exporters.export(part, "tube_mm.stl")

print("STL exporté en millimètres.")
