com = g++
srcf = src
binf = build
hdf = include #headers folder
app = musicman

obj = 

aopt =-L/usr/include/ -lboost_program_options#application compilation options

$(app): $(binf)/$(obj) $(srcf)/main.cpp
	$(com) -o $(app) $(srcf)/main.cpp $(aopt) && mv $(app) $(binf)
run:
	./$(binf)/$(app)
clean:
	rm ./$(binf)/*
