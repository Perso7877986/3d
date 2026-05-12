import cadquery as cq
from cadquery import exporters

# Dimensions en cm
outer_diameter = 3.9
inner_diameter = 2.8
height = 1.5

# Création du tube
part = (
    cq.Workplane("XY")
    .circle(outer_diameter / 2)
    .circle(inner_diameter / 2)
    .extrude(height)
)

# Export STEP
exporters.export(part, "tube.step")

# Export STL
exporters.export(part, "tube.stl")

print("Fichiers STEP et STL créés.")