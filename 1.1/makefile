com = g++
srcf = src
binf = build
hdf = include #headers folder
app = musicman

obj = 

aopt = -Wall -L/usr/include -lboost_system -lboost_program_options #application compilation options

$(app): $(binf)/$(obj) $(srcf)/main.cpp
	$(com) $(aopt) $(obj) -o $(app) $(srcf)/main.cpp
