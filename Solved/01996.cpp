#include <iostream>
#include <queue>
#include<stdlib.h>
using namespace std;
int M[1002][1002];
int S[1002][1002];

int main() {
	queue< pair<int, int> >q;
	queue<int> w;
	int n;
	char tmp;
	cin >> n;
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++) {
			cin >> tmp;
			if (tmp == '.')
				M[i][j] = 0;
			 else 
				M[i][j]=tmp-'0';
		}
	
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
			for (int a = -1; a <= 1; a++)
				for (int b = -1; b <= 1; b++)
					S[i][j] += M[i + a][j + b];

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			if (M[i][j] != 0)
				cout << "*";
			else if (S[i][j] > 9)
				cout << "M";
			else
				cout << S[i][j];
		}
			
		cout << endl;
	}
}

