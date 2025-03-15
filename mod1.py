val = 10
PI = 3.141592
def randint(x):
	return 3 * x + 5
class Calculator:
    # 객체생성시에 자동으로 실행되는 메서드 : 생성자
	def __init__(self, first, second): # 멤버변수에 초기값을 주기위한 메서드
		self.first = first
		self.second = second
	def add(self):
		self.result = self.first + self.second
		return self.result
calc = Calculator(10,30)