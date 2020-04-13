# Print out all of the strings in the following array in alphabetical order, each on a separate line.
arr = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']
# The expected output is:
# 'Cha Cha'
# 'Foxtrot'
# 'Jive'
# 'Paso Doble'
# 'Rumba'
# 'Samba'
# 'Tango'
# 'Viennese Waltz'
# 'Waltz'
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

sorted_arr = sorted(arr)

for i in sorted_arr:
    print(i)


print()
print()


# Print out all of the strings in the following array in alphabetical order sorted by the middle letter of each string, each on a separate line. If the word has an even number of letters, choose the later letter, i.e. the one closer to the end of the string.
arr = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']
# The expected output is:
# 'Cha Cha'
# 'Paso Doble'
# 'Viennese Waltz'
# 'Waltz'
# 'Samba'
# 'Rumba'
# 'Tango'
# 'Foxtrot'
# 'Jive'
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

8
4
# len(string) // 2

9 // 2
4

123456789

def func(string):
    return string[len(string) // 2]

arr.sort(key = func)

for i in arr:   
    print(i)

