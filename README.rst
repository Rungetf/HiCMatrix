HiCMatrix
===========

This library implements the central class of HiCExplorer to manage Hi-C interaction matrices. It is separated from the main project to enable to use of Hi-C matrices
in other project without the dependency to HiCExplorer. Moreover, it enables us to use the already separated pyGenomeTracks (former hicPlotTADs) to be used in HiCExplorer
because mutual dependencies are resolved.
