import importlib
import logging
log = logging.getLogger(__name__)


class MatrixFileHandler():
    """
    This class handles the load and save of the different Hi-C contact matrix formats.
    """

    def __init__(self, pFileType='cool', pMatrixFile=None, pChrnameList=None,
                 pApplyCorrectionCooler=None, pBedFileHicPro=None, pCorrectionFactorTable=None,
                 pCorrectionOperator=None, pEnforceInteger=None):

        self.class_ = getattr(importlib.import_module('.' + pFileType.lower(), package='hicmatrix.lib'), pFileType.title())

        if pFileType == 'hicpro':
            self.matrixFile = self.class_(pMatrixFile=pMatrixFile, pBedFile=pBedFileHicPro)
        else:
            self.matrixFile = self.class_(pMatrixFile)
            if pFileType == 'cool':
                self.matrixFile.chrnameList = pChrnameList
                if pCorrectionFactorTable is not None:
                    self.matrixFile.correctionFactorTable = pCorrectionFactorTable
                if pCorrectionOperator is not None:
                    self.matrixFile.correctionOperator = pCorrectionOperator
                if pEnforceInteger is not None:
                    self.matrixFile.enforceInteger = pEnforceInteger

    def load(self):

        return self.matrixFile.load()

    def set_matrix_variables(self, pMatrix, pCutIntervals, pNanBins, pCorrectionFactors, pDistanceCounts):
        self.matrixFile.set_matrix_variables(pMatrix, pCutIntervals, pNanBins, pCorrectionFactors, pDistanceCounts)

    def save(self, pName, pSymmetric, pApplyCorrection):
        self.matrixFile.save(pName, pSymmetric, pApplyCorrection)

    def load_init(self):
        pass
