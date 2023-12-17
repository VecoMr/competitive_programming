#include <array>
#include <iostream>

class Matrix2x2 {
public:
    std::array<std::array<int, 2>, 2> matrix;
    Matrix2x2(int a, int b, int c, int d) {
        matrix[0][0] = a;
        matrix[0][1] = b;
        matrix[1][0] = c;
        matrix[1][1] = d;
    }

    Matrix2x2 operator*(const Matrix2x2& other) const {
        Matrix2x2 result(0, 0, 0, 0);
        for (int i = 0; i < 2; ++i) {
            for (int j = 0; j < 2; ++j) {
                for (int k = 0; k < 2; ++k) {
                    result.matrix[i][j] += this->matrix[i][k] * other.matrix[k][j];
                }
            }
        }
        return result;
    }

    Matrix2x2 power(int exponent) {
        Matrix2x2 result(1, 0, 0, 1);
        Matrix2x2 base = *this;
        while (exponent) {
            if (exponent & 1) {
                result = result * base;
            }
            base = base * base;
            exponent >>= 1;
        }
        return result;
    }
};

int main(void) {
    int n = 0;
    int b = 0;

    while (std::cin >> n >> b) {
        Matrix2x2 mat(1, 1, 1, 0);
        mat = mat.power(n);
        std::cout << mat.matrix[0][0] << " " << mat.matrix[1][0] << std::endl;
    }

}