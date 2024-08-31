import pytest
from main import *


@pytest.mark.parametrize(
	"input_brackets, expected", (
			['(((([{}]))))', 'Сбалансированно'],
			['[([])((([[[]]])))]{()}', 'Сбалансированно'],
			['{{[()]}}', 'Сбалансированно'],
			['}{}', 'Несбалансированно'],
			['{{[(])]}}', 'Несбалансированно'],
			['[[{())}]', 'Несбалансированно'],
	)
)
def test_check_balance_brackets(input_brackets, expected):
	assert stack.check_balance_brackets(input_brackets) == expected
