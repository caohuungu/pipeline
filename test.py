#Hello John Doe. Your current balance is $53.44.
data = ("John", "Doe", 53.44)
format_string = "Hello"

print(format_string + " %s %s. Your current balance is %.2f." % data)