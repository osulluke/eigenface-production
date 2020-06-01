main: main.cpp img-display.cpp
	g++ main.cpp -o main -larmadillo -llapack -lblas
	g++ img-display.cpp -o img-display `pkg-config --cflags --libs opencv4`
	wget -O ~/linuxconfig_logo.png https://linuxconfig.org/images/linuxconfig_logo.png
	./main
	./img-display ~/linuxconfig_logo.png

setup:


clean:
	rm main img-display