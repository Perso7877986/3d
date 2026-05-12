import cadquery as cq
from cadquery import exporters

# Dimensions in cm
outer_diameter = 3.9
inner_diameter = 2.8
height = 1.5

# Create hollow cylinder
part = (
    cq.Workplane("XY")
    .circle(outer_diameter / 2)
    .circle(inner_diameter / 2)
    .extrude(height)
)

# Export STEP file
exporters.export(part, "tube_3_9_2_8_h1_5.step")

print("STEP file created.")
