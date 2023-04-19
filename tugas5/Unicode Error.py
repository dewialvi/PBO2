s1 = 'Hello, \xff\xfeW\x00o\x00r\x00l\x00d\x00'
s2 = 'Hello, World'

print(s1.encode('utf-8'))
print(s2.encode('utf-8'))
