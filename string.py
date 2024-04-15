text = 'это моя строка'
temp_text = ''.join(reversed(text))
new_text = 'это новая строка'

print(text[0])
print(text[-1])
print(text[3:6])
print(temp_text)
print(f'lenght of "text" string is: {len(text)}')
print(f'{new_text} {text}')
