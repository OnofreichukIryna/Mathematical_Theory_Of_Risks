#include <iostream>
#include <limits> // for std::numeric_limits
using namespace std;

int main() {
    double probRain;
    cout << "Input probability of rain (from 0 to 1): ";
    while (!(cin >> probRain) || probRain < 0 || probRain > 1) {
        cout << "Invalid input! Enter the probability of rain (from 0 to 1): ";
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    double UtilityHomeRain, UtilityHomeSun;
    cout << "Rating of staying home during rain: ";
    while (!(cin >> UtilityHomeRain)) {
        cout << "Invalid input! Enter a numeric value: ";
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    cout << "Rating of staying home during sunshine: ";
    while (!(cin >> UtilityHomeSun)) {
        cout << "Invalid input! Enter a numeric value: ";
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    double UtilityForestRain, UtilityForestSun;
    cout << "Rating of going to the forest during rain: ";
    while (!(cin >> UtilityForestRain)) {
        cout << "Invalid input! Enter a numeric value: ";
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    cout << "Rating of going to the forest during sunshine: ";
    while (!(cin >> UtilityForestSun)) {
        cout << "Invalid input! Enter a numeric value: ";
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    double W_home = probRain * UtilityHomeRain + (1 - probRain) * UtilityHomeSun;
    double W_forest = probRain * UtilityForestRain + (1 - probRain) * UtilityForestSun;

    cout << "Utility of staying home: " << W_home << endl;
    cout << "Utility of going to the forest: " << W_forest << endl;

    if (W_home > W_forest) {
        cout << "It is recommended to stay home" << endl;
    }
    else {
        cout << "It is recommended to go to the forest" << endl;
    }

    return 0;
}
