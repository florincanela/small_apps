import re

#at least 8 char long
#must end with a digit
#cand contain only %$#@
pattern = re.compile(r"^[\w%$#@]{7,}\d$")
password = '12345678'


print(pattern.fullmatch(password))