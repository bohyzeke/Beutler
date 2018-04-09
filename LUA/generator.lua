
off = 20
ttt = 79

temp = math.randomseed(os.time())
math.random()
math.random()
math.random()
CodeA = 0
for i=1,4 do
	CodeA = (off + math.random(ttt)) + CodeA * 100
end
print(CodeA)



