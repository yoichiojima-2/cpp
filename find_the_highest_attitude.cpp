// 1732. Find the Highest Altitude

// There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes.
// The biker starts his trip on point 0 with altitude equal 0.
// You are given an integer array gain of length n where gain[i] is the net gain in altitude
// between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

#include <iostream>
#include <vector>

using namespace std;


int solution(const vector<int>& gain) {
    int idx = 0;
    int altitude = 0;
    int max_altitude = 0;

    cout << "idx: " << idx << endl;
    cout << "altitude: " << altitude << endl;
    cout << "max_altitude: " << max_altitude << endl << endl;

    for (int i : gain) {
        idx += 1;
        altitude += i;
        max_altitude = max(altitude, max_altitude);
        cout << "idx: " << idx << endl;
        cout << "altitude: " << altitude << endl;
        cout << "max_altitude: " << max_altitude << endl << endl;
    }

    return max_altitude;
}

int main() {
    vector<vector<int>> gain = { {1, 2, -3, 4}, {0, -4, -3, -2, -1, 4, 3, 2} };
    for (vector<int> i : gain) {
        int result = solution(i);
        cout << "RESULT: " << result << endl << endl;
    }

    return 0;
}
