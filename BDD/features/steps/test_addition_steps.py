from behave import given, when, then
from test_unit_sum import add  # Assuming add is defined in a module named 'addition'


@given('I have the numbers {a:d} and {b:d}')
def step_given_i_have_numbers(context, a, b):
    context.a = a
    context.b = b


@when('I add the numbers')
def step_when_i_add_the_numbers(context):
    context.result = add(context.a, context.b)


@then('the result should be {expected_result:d}')
def step_then_result_should_be(context, expected_result):
    assert context.result == expected_result, f"Expected {expected_result} but got {context.result}"
