def concatenate(**words):
	result = ""
	for arg in words.values():
		result += arg
	return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
