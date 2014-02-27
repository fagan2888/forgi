from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(name='forgi',
      version='0.1',
      description='RNA Graph Library',
      author='Peter Kerpedjiev',
      author_email='pkerp@tbi.univie.ac.at',
      url='http://www.tbi.univie.ac.at/~pkerp/forgi/',
      packages=['forgi', 'forgi.graph', 'forgi.threedee', 'forgi.threedee.model', 
                'forgi.utilities', 'forgi.threedee.utilities', 'forgi.aux', 
                'forgi.aux.k2n_standalone', 'forgi.threedee.visual'],
      package_data={'forgi.threedee': ['data/*.pdb']},
      scripts=['examples/visualize_cg.py', 'examples/visualize_pdb.py', 
               'examples/pdb_to_cg.py'],
      cmdclass = {'build_ext': build_ext},
      ext_modules = [Extension("forgi.threedee.utilities.cytvec", ["forgi/threedee/utilities/cytvec.pyx"], include_dirs=['.'])]
     )
