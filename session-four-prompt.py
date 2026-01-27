class favAnimal:
	def __init__(self, arms, legs, eyes, furry, tail):

		self.arms = arms
		self.legs = legs
		self.eyes = eyes
		self.furry = furry
		self.tail = tail
	def describe(self):
		print("Description")
		print(f"Arm Length: {self.arms}")
		print(f"Leg Length: {self.legs}")
		print(f"Eye Number: {self.eyes}")
		print(f"Furry?: {self.furry}")
		print(f"Tail?: {self.tail}")

favAnimal1 = favAnimal(2.55, 4.67, 2, False, True)
favAnimal1.describe()

