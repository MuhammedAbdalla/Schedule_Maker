all:
	g++ -std=c++17 scheduler.cpp -o scheduler -g
clean:
	rm scheduler