# Python program to implement stack to check for balanced paranthesis

# Function to check if parenthesis are balanced
def balanced_paranthesis(str):
	stack = []

	for char in str:
		if char in ["(", "{", "["]:
			# If opening paranthesis, push to stack
			stack.append(char)
        
		else:
			# If closing paranthesis, stack cannot be empty
			if len(stack) == 0:
				return False
            
			top_char = stack.pop()

			if top_char == '(':
				if char != ")":
					return False
            
			if top_char == '{':
				if char != "}":
					return False
            
			if top_char == '[':
				if char != "]":
					return False

	# Check if stack is empty
	if len(stack) == 0:
		return True
	return False


unbalanced_str = "{()}[)"
balanced_str = "{()()}[]"

print(balanced_paranthesis(balanced_str))
print(balanced_paranthesis(unbalanced_str))
