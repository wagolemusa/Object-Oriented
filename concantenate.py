def concatenate(**kwargs):
	result = ""
	# Iterating over the Python kwargs dictionary
	for arg in kwargs.values():
	 	result += arg

	return result

print(concatenate(a="Real", b="Python", c="is", d="Great", e="!"))