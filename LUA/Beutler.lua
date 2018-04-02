


off = 20
ttt = 79

math.randomseed(os.time())
math.random()
math.random()
math.random()

function generateB(CA)
	A4 = CodIn % 100
--	print(A4)
	CA = math.floor(CA / 100)
	A3 = CA % 100
--	print(A3)
	CA = math.floor(CA / 100)
	A2 = CA % 100
--	print(A2)
	CA = math.floor(CA / 100)
	A1 = CA % 100
--	print(A1)
--	print()
	CB = 0
	CB = (A1 % 11*4) + CB * 100
	CB = (A2 % 13*3) + CB * 100
	CB = (A3 % 17*2) + CB * 100
	CB = (A4 % 19*1) + CB * 100

	print ("codeB = ".. CB )
	return CB
end



while true do
	odpo = ""
	print ("Napis codeA ")

	CodIn = tonumber(io.read())
	print(CodIn)

	if type( CodIn) == "nil"	then
		CodeA = 0
		CodeA = (off + math.random(ttt)) + CodeA * 100
		CodeA = (off + math.random(ttt)) + CodeA * 100
		CodeA = (off + math.random(ttt)) + CodeA * 100
		CodeA = (off + math.random(ttt)) + CodeA * 100
		CodIn = CadeA
		print(CodeA)
	else
	  CodIn = math.floor(CodIn)
	  generateB(CodIn)
	end
	print("Dalsi kod y/n")
	odpo = io.read()
	if odpo == "n" then
		break
	end

end



CodIn = io.read()
