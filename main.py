class Stack:
	def __init__(self):
		self.stack = []

	def is_empty(self):
		return self.stack == []

	def push(self, item):
		return self.stack.append(item)

	def pop(self):
		if self.is_empty():
			return None
		removed = self.stack.pop()
		return removed

	def peek(self):
		return self.stack[-1]

	def size(self):
		return len(self.stack)

	def check_balance_brackets(self, text: str) -> bool():
		open_brackets = ['(', '[', '{']
		close_brackets = [')', ']', '}']
		for bracket in text:
			if bracket in open_brackets:
				stack.push(open_brackets.index(bracket))
			elif bracket in close_brackets:
				if self.stack and stack.peek() == close_brackets.index(bracket):
					stack.pop()
				else:
					return 'Несбалансированно'
		return 'Сбалансированно'


__name__ = '__main__'
stack = Stack()
