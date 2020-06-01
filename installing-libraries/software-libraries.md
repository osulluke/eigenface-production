# Setting up the development environment
1. This is a list of libraries that I think we'll need in order to develop this project
2. You can look through all the items below
3. When you're ready, you can install all the libraries below by running `./install-lib.sc` or you can manually install everything that is listed below with the sudo commands; if you want to use the install script, you may have to run `chmod 755 install-lib.sc` in order to make it executable.
4. Right now, I can't get OpenCV (C++) to display the image that is downloaded through the XServer; if anyone has any ideas, let me know. I think this will be pretty important.
5. What will be installed are Linear Algebra libraries (Eigen, Armadillo), and OpenCV (for C++ and Python3); there are a couple at the very bottom that aren't required, but which I installed because I like one of them (tree) and the x11-xserver-utils I downloaded in an attempt to get the image display program to work. 

## Install Eigen (C++ Linear Algebra/Matrix library)
sudo apt install libeigen3-dev -y
> http://eigen.tuxfamily.org/index.php?title=Main_Page

## Install supporting libaries for Armadillo (Linear Algebra library)
sudo apt install libopenblas-dev liblapack-dev libarpack2-dev libsuperlu-dev -y
> http://arma.sourceforge.net/download.html
> https://tutorialforlinux.com/2020/04/23/step-by-step-armadillo-ubuntu-20-04-installation/
> https://medium.com/@romanpoya/a-look-at-the-performance-of-expression-templates-in-c-eigen-vs-blaze-vs-fastor-vs-armadillo-vs-2474ed38d982

## Install Armadillo - do the step above first!
sudo apt install libarmadillo-dev -y
> https://launchpad.net/ubuntu/+source/armadillo/
> http://arma.sourceforge.net/docs.html#example_prog
> https://solarianprogrammer.com/2017/03/24/getting-started-armadillo-cpp-linear-algebra-windows-mac-linux/
> https://www.uio.no/studier/emner/matnat/fys/FYS4411/v13/guides/installing-armadillo/

## Install OpenCV (Video processing/Matrix library C++)
sudo apt install libopencv-dev 
sudo apt install python3-opencv
> https://linuxconfig.org/install-opencv-on-ubuntu-18-04-bionic-beaver-linux
> https://linuxize.com/post/how-to-install-opencv-on-ubuntu-18-04/

## Not required, but I installed 'tree' (displays directories on command line)
sudo apt install tree -y
sudo apt install x11-xserver-utils
