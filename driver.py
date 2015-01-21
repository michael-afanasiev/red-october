#!/usr/bin/env python

import cubit_com

# Initialize the communicator.
communicator = cubit_com.communicator()

# Generate the hollow spheres. Radii in kilometeres.
communicator.generate_hollow_sphere(6371, 5961)
communicator.generate_hollow_sphere(5961, 5711)
communicator.generate_hollow_sphere(5711, 3482)
communicator.generate_hollow_sphere(3482, 1218)
communicator.generate_sphere(1218)

# Set up meshing parameters and mesh.
communicator.set_mesh_type('tetmesh')
communicator.imprint_merge()
communicator.set_mesh_size('300')
communicator.mesh_all_volumes()

# Refine.
communicator.refine_around_vertex(20218, 50, bias=3.0)

# Export file.
communicator.export_abaqus()
communicator.export_exodus()