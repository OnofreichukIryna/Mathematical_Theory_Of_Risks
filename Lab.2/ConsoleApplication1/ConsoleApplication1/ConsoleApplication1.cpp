#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

typedef vector<vector<double>> Matrix;
typedef vector<double> Vec;

// Функція для виведення вектора
void print_vector(const Vec& v) {
    for (double val : v) {
        cout << val << " ";
    }
    cout << endl;
}

// Метод Гаусса для розв'язку системи рівнянь
Vec gauss(Matrix A, Vec y) {
    int n = y.size();

    // Прямий хід
    for (int i = 0; i < n; i++) {
        // Пошук головного елемента
        int max_row = i;
        for (int k = i + 1; k < n; k++) {
            if (fabs(A[k][i]) > fabs(A[max_row][i])) {
                max_row = k;
            }
        }

        // Заміна рядків
        swap(A[i], A[max_row]);
        swap(y[i], y[max_row]);

        // Прямий хід: обнуляємо нижні елементи стовпця
        for (int j = i + 1; j < n; j++) {
            double factor = A[j][i] / A[i][i];
            for (int k = i; k < n; k++) {
                A[j][k] -= factor * A[i][k];
            }
            y[j] -= factor * y[i];
        }
    }

    // Зворотний хід
    Vec x(n);
    for (int i = n - 1; i >= 0; i--) {
        x[i] = y[i];
        for (int j = i + 1; j < n; j++) {
            x[i] -= A[i][j] * x[j];
        }
        x[i] /= A[i][i];
    }

    return x;
}

int main() {
    // Початкова матриця A
    Matrix A = {
        {0.15, 0.12, 0.04, 0.3},
        {0.27, 0.07, 0.12, 0.22},
        {0.31, 0.24, 0.30, 0.11},
        {0.14, 0.05, 0.16, 0.21}
    };

    // Вектор вільних членів y
    Vec y = { 135.39, -83.47, -31.31, 211.78 };

    // Створюємо одиничну матрицю і модифікуємо A
    for (int i = 0; i < A.size(); i++) {
        A[i][i] -= 1.0;  // A - I
        y[i] = -y[i];    // -y
    }

    // Розв'язок системи
    Vec x = gauss(A, y);

    // Виведення результату
    cout << "Розв'язок системи: ";
    print_vector(x);

    return 0;
}