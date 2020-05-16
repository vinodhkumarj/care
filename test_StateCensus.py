import pytest

import StateCensus

from test_programs.CustomExceptions import CensusAnalysisException
from test_programs.StateCensus import StateCensusAnalyser
from test_programs.StateCodeData import StateCodeAnalyser

file_path = "C:\\Python\\test_programs\\StateCensusData.csv"
wrong_file_path = "C:\\Python\\test\\StateCensusData.csv"
wrong_file = "C:\\Python\\test_programs\\StateCensusData.txt"
header_file = "C:\\Python\\test_programs\\statecensus.csv"
state_code_path = "C:\\Python\\test_programs\\StateCode.csv"
state_header_file = "C:\\Python\\test_programs\\StateCode.1.csv"

class TestCensusAnalyser:
    def test_TheCensusCodesCsvFile_IfHasCorrectNumberOfRecords_ShouldReturnTrue(self):
        stateCensusAnalyser = StateCensusAnalyser()
        records = stateCensusAnalyser.loadCensusData(file_path)
        assert records == 29

    def test_WrongCensusCsvFile_CheckPresentOrNot_ShouldThrowException(self):
        try :
            stateCensusAnalyser = StateCensusAnalyser()
            records = stateCensusAnalyser.loadCensusData(wrong_file_path)
        except Exception as exception:
            assert type(exception) == CensusAnalysisException

    def test_DifferentTypeFile_CheckPresentOrNot_ShouldThrowException(self):
        try:

            stateCensusAnalyser = StateCensusAnalyser()
            records = stateCensusAnalyser.loadCensusData(wrong_file)
        except Exception as e:
            assert type(e) == CensusAnalysisException

    def test_StateCensusDataFile_WhenDelimiterIncorrect_ShouldThrowException(self):
        try:
            stateCensusAnalyser = StateCensusAnalyser()
            records = stateCensusAnalyser.loadCensusData(header_file)
        except Exception as exception:
            assert type(exception) == CensusAnalysisException

    def test_TheStateCodesCsvFile_IfHasCorrectNumberOfRecords_ShouldReturnTrue(self):
        stateCodeAnalyser = StateCensusAnalyser()
        records = stateCodeAnalyser.loadCensusData(state_code_path)
        assert records == 37

    def test_WrongStateCodeCsvFile_CheckPresentOrNot_ShouldThrowException(self):
        try :
            stateCodeAnalyser = StateCodeAnalyser()
            records = stateCodeAnalyser.loadStateCodeData(wrong_file_path)

        except Exception as exception:
            assert type(exception) == CensusAnalysisException

    def test_DifferentTypeCodeFile_CheckPresentOrNot_ShouldThrowException(self):
        try:
            stateCodeAnalyser = StateCodeAnalyser()
            records = stateCodeAnalyser.loadStateCodeData(wrong_file)

        except Exception as e:
            assert type(e) == CensusAnalysisException

    def test_StateCodeFile_WhenDelimiterIncorrect_ShouldThrowException(self):
        try:
            stateCodeAnalyser = StateCodeAnalyser()
            records = stateCodeAnalyser.loadStateCodeData(state_header_file)
        except Exception as exception:
            assert type(exception) == CensusAnalysisException







