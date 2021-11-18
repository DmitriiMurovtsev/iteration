class FlatIterator:
	def __init__(self, my_list):
		self.my_list = []
		self.receive_items(my_list)
		self.cursor = -1
		self.end = len(self.my_list)

	def receive_items(self, item_list):
		for item in item_list:
			if type(item) == list:
				self.receive_items(item)
			else:
				self.my_list.append(item)

	def __iter__(self):
		return self

	def __next__(self):
		self.cursor += 1
		if self.cursor == self.end:
			raise StopIteration
		return self.my_list[self.cursor]


def get_all_items(my_list):
	for item in my_list:
		if type(item) == list:
			yield from get_all_items(item)
		else:
			yield item


nested_list = [[['a', [1, ['b', 2]]], 'c', 3], ['d', 4, 'e'], [5, 'f', None], 0, 1, 2, 3, 4]

for item in FlatIterator(nested_list):
	print(item)

for item in get_all_items(nested_list):
	print(item)
