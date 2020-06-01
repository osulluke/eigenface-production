#include <iostream>
#include <eigen3/Eigen/Dense>
#include <armadillo>

using Eigen::MatrixXd;
using namespace arma;

void test_Eigen_Install();
void test_Armadillo_Install();

int main() {
    test_Eigen_Install();
    test_Armadillo_Install();

    return 0;
}

void test_Eigen_Install() {
    std::cout << "Print out Eigen3 Matrix: " << std::endl;
    MatrixXd m(2,2);
    m(0,0) = 3;
    m(1,0) = 2.5;
    m(0,1) = -1;
    m(1,1) = m(1,0) + m(0,1);
    std::cout << m << std::endl;
    std::cout << "Eigen 3 installed successfully!\n" << std::endl;

    return;
}

void test_Armadillo_Install() {
    std::cout << "Print out Armadillo Matrix: " << std::endl;
    mat A = randu<mat>(4,5);
    mat B = randu<mat>(4,5);

    std::cout << A*B.t() << std::endl;
    std::cout << "Armadillo installed successfully!" << std::endl;

    return;
}