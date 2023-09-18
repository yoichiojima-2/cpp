#include <iostream>

using namespace std;

int main() {
    int sales = 95000;
    double state_tax = 0.04;
    double country_tax = 0.02;

    double state_tax_to_pay = sales * state_tax;
    double country_tax_to_pay = sales * country_tax;

    cout << "country tax: " << country_tax_to_pay << endl;
    cout << "state_tax: " << state_tax_to_pay << endl;
    cout << "income: " << sales - country_tax_to_pay - state_tax_to_pay;

    return 0;
}