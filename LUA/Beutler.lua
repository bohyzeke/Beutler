


off = 20
ttt = 79

math.randomseed(os.time())
math.random()
math.random()
math.random()

-- generovanie koduB z koduA

function generateB(CA)
	A4 = CA % 100
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


--hlavna program
while true do
	odpo = ""
	print ("Napis codeA ")
	CodIn = tonumber(io.read())

	-- generovanie nahodneho koduA
	if type( CodIn) == "nil"	then
		CodeA = 0
		for i= 1,4 do
			CodeA = (off + math.random(ttt)) + CodeA * 100
		end
		CodIn = math.floor(CodeA)
	end

	print("CodeA = " .. CodIn)

	generateB(CodIn)  			-- generovanie koduB

	print("Dalsi kod y/n")
	odpo = io.read()
	if odpo == "n" then
		break
	end

end


