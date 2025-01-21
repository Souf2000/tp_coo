CXX = g++
CXXFLAGS = -Wall -std=c++17 -I/usr/local/include -I/usr/include/nlohmann

all: main

main: main.o Ville.o Objet.o Local.o SiegeSocial.o
	$(CXX) $(CXXFLAGS) -o main main.o Ville.o Objet.o Local.o SiegeSocial.o -lcpr

main.o: main.cpp Ville.h Objet.h Local.h SiegeSocial.h
	$(CXX) $(CXXFLAGS) -c main.cpp

Ville.o: Ville.cpp Ville.h
	$(CXX) $(CXXFLAGS) -c Ville.cpp

Objet.o: Objet.cpp Objet.h
	$(CXX) $(CXXFLAGS) -c Objet.cpp

Local.o: Local.cpp Local.h
	$(CXX) $(CXXFLAGS) -c Local.cpp

SiegeSocial.o: SiegeSocial.cpp SiegeSocial.h
	$(CXX) $(CXXFLAGS) -c SiegeSocial.cpp

clean:
	rm -f *.o main

