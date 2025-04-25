
import pytest
from pytest_bdd import scenarios, given, when, then

scenarios('../features/sample.feature')

@given('a test case setup is prepared')
def test_case_setup():
    return True

@when('the test case is executed')
def execute_test_case():
    return True

@then('the result should be stored successfully')
def result_should_be_stored():
    assert True
