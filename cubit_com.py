#!/usr/bin/env python

import sys

try:
    import cubit
except ImportError:
    raise ImportError('The cubit python module was not found. Exit.')
    
class communicator:
    
    def __init__(self):
        """
        Attempts to initialize the cubit instance.
        """
        
        cubit.init('.')
        
    def set_mesh_type(self, type):
        """
        Sets the mesh type for all constructed volumes. Exits if there are no
        volumes present. 
        
        :type: String specifiying either 'tetmesh' or 'hex'.
        """
        
        supported_types = ['tetmesh', 'hex']
        
        if type not in supported_types:
            sys.exit ('Mesh type not supported. Choose tet or hex. EXITING.')
            
        cubit.cmd('vol all scheme ' + type)
            
    def imprint_merge(self):
        """
        Performs an imprint and merge on all volumes.
        """
    
        cubit.cmd('imprint all')
        cubit.cmd('merge all')
        
    def execute_command(self, command):
        """
        Executes a command using cubit.cmd.
        
        :command: A string to pass to cubit (i.e. create brick x10).
        """
        
        cubit.cmd(command)
        
    def generate_sphere(self, rad):
        """
        Generates a sphere of a given radius.
        
        :rad: Radius of (solid) sphere.
        """
        
        string = 'Create sphere radius ' + str(rad)
        cubit.cmd (string)
        
    def generate_hollow_sphere(self, top_rad, bot_rad):
        """
        Asks cubit to generate a hollow sphere.
    
        :param top_rad: The maxiumum radius of the hollow chunk.
        :param bot_rad: The minimum radius of the hollow chunk.
        """
    
        string = 'Create sphere radius ' + str(top_rad) + ' inner radius ' \
        + str(bot_rad)
        cubit.cmd(string)
        
    def set_mesh_size(self, size):
        """
        Attempts to set an edge length for a volume. Since cubit is weird,
        we do this redunantly (vol, surf, curve). Safer. Also sets a strict
        constant sizing function.
        
        :size: Desired edge length (in km).
        """
        
        cubit.cmd('vol all size ' + size)
        cubit.cmd('surf all size ' + size)
        
        cubit.cmd('vol all sizing function constant')
        cubit.cmd('surf all sizing function constant')
        
    def mesh_all_volumes(self):
        """
        Goes ahead and attempts to mesh all the volumes. No current way to deal
        with mesh failures. Again, we do this in a surface - volume manner. This
        should be redundant, but again cubit is a strange beast and it seems
        more stable this way.
        """
        
        cubit.cmd('mesh surf all')
        cubit.cmd('mesh vol all')
        
    def export_facets(self, filepath="./tetrahedra.fac"):
        """
        Exports a facets file to a directory.
        
        :filepath: Directory to write files to. Defaults to current directory.
        """
    
        cubit.cmd('export facets "' + filepath + '" overwrite')
        
    def export_exodus(self, filepath="./tetrahedra.ex2"):
        """
        Export an exodus file to a directory.
        
        :filepath: Directory to write files to. Defaults to current directory.
        """
        
        cubit.cmd('export mesh "' + filepath + '" overwrite')
        
    def export_abaqus(self, filepath="./tetrahedra.inp"):
        """
        Export an ABAQUS file to a directory.
        
        :filepath: Directory to write files to. Defaults to current directory.
        """
        
        cubit.cmd ('export abaqus "' + filepath + '" overwrite cubitids')
        
    def refine_around_vertex(self, node, size, bias=1.0):
        """
        Refines the elements around a particular node.
        
        :vertex: Vertex number, provided by the user, around which the
        refinement is desired.
        :size: Requested size of node.
        :bias: Relative amount by which elements may increase in size around
        refinement point. Default to 1.
        """
        
        cubit.cmd('Refine Node %d Size %d Bias %d Smooth' % (node, size, bias))