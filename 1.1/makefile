com = g++
srcf = src
binf = build
hdf = include#headers folder
app = musicman

obj = metadata.o

aopt =-L/usr/include/ -lboost_program_options#application compilation options

$(app): $(binf)/$(obj) $(srcf)/main.cpp
	$(com) -o $(app) $(obj) $(srcf)/main.cpp $(aopt) && mv $(app) *.o $(binf)
$(binf)/metadata.o: $(srcf)/metadata.cpp $(hdf)/metadata.hpp
	$(com) $(srcf)/metadata.cpp -c
run:
	./$(binf)/$(app)
clean:
	rm ./$(binf)/*
