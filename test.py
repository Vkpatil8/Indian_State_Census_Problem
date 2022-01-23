import indian_State_Census


def test_number_of_record():
    result = indian_State_Census.StateCensusAnalyser.count_number_of_records()
    expected = 30
    assert expected == result
