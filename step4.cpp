#include <bits/stdc++.h>

int N;
double buff, maxSum = 2 * 10e5, aInd, bInd;
std::vector<double> arr;
int main() {
    std::cin >> N;
    for(int i = 0; i < N; i++){
        std::cin >> buff;
        arr.push_back(buff);
    }

    for(int i = 0; i < arr.size() - 1; i++){
         double sumA = 0, sumB = 0;
         for(int j = 0; j < i + 1; j++){
             sumA += arr[j];
         }
         for(int j = i + 1; j < arr.size(); j++){
             sumB += arr[j];
         }
         double a = sumA / (i + 1);
         double b = sumB / (arr.size() - i - 1);

         double deltaA = 0, deltaB = 0;
         for(int j = 0; j < i + 1; j++){
             if(a < arr[j]){
                 deltaA += arr[j] - a;
             }
         }
         for(int j = i + 1; j < arr.size(); j++){
             if(b < arr[j]){
                 deltaB += arr[j] - b;
             }
         }
         if(deltaA + deltaB < maxSum){
             maxSum = deltaA + deltaB;
             aInd = i + 1;
             bInd = arr.size() - i - 1;
         }
    }
    std::cout << aInd << ' ' << bInd;
    return 0;
}
