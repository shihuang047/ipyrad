#!/usr/bin/env python

# version is the same as ipyrad
from ipyrad import __version__

# analysis tools will have a class object that is upper case, which is 
# called by a convenience function which is lower case, and has the 
# same name as the module (file), such that when we import the function
# it clobbers the file name as the import. 

# installed alonside ipyrad: conda install ipyrad -c eaton-lab
#from tetrad import Tetrad

# conda install raxml mrbayes -c bioconda
from .raxml import Raxml as raxml
from .mrbayes import MrBayes as mrbayes
from .treeslider import TreeSlider as treeslider
from .clade_weights import CladeWeights as clade_weights
# from .twisst import Twisst as twisst

# conda install structure clumpp -c ipyrad
from .structure import Structure as structure
#from .pca import pca

# conda install tetrad -c eaton-lab
#from .tetrad import Tetrad as tetrad

# conda install bucky -c ipyrad
# conda install mrbayes -c bioconda
from .bucky import Bucky as bucky

# conda install bpp -c ipyrad
from .bpp import Bpp as bpp

# conda install sratools -c bioconda
# from .sratools import SRA as sratools

# no requirements
# from .baba import Baba as baba
from .digest_genome import DigestGenome as digest_genome
#from .popgen import Popgen as popgen
#from .treemix import Treemix as treemix
