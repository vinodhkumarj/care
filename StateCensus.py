from sys import argv

import pandas as pd

from test_programs.CustomExceptions import CensusAnalysisException


class StateCensusAnalyser:

    def loadCensusData(self,file):
        try:
            df = pd.read_csv(file)
            number = df['State'].count()
            return number
        except Exception as exception:
            raise CensusAnalysisException("please enter proper file path")



