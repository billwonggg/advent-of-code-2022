#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    int mx = 0;
    int sum = 0;
    string tmp;
    vector<int> calories;
    while (getline(cin, tmp)) {
        if (tmp.empty()) {
            calories.push_back(sum);
            sum = 0;
        } else {
            sum += stoi(tmp);
        }
    }
    if (sum != 0) calories.push_back(sum);

    sort(calories.begin(), calories.end());

    cout << "The top 3 are:\n"
         << calories[calories.size() - 1] << '\n'
         << calories[calories.size() - 2] << '\n'
         << calories[calories.size() - 3] << '\n'
         << "Sum of top 3 is: "
         << calories[calories.size() - 1] + calories[calories.size() - 2] +
                calories[calories.size() - 3]
         << "\n";
}