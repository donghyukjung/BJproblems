#include <iostream>
#include <queue>
using namespace std;
int M[1000][1000];
int W[1000][1000];


int main() {
	queue< pair<int, int> >q;
	queue<int> w;
	int m, n;
	cin >> n >> m;
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= m; j++) cin >> M[i][j];
	int sx, sy;
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= m; j++) 
			if (M[i][j] == 2) {
				sx = i, sy = j;
				break;
			}
	int len=0;
	q.push(make_pair(sx, sy));
	w.push(len);
	while (!q.empty()) {
		pair<int, int> p = q.front();
		int val = w.front();
		int x = p.first;
		int y = p.second;
		q.pop();
		w.pop();
		if (M[x][y] == 0 || (!(x == sx && y == sy) && W[x][y] != 0)) continue;
		W[x][y]=val++;
		w.push(val);
		w.push(val);
		w.push(val);
		w.push(val);
		q.push(make_pair(x+1, y));
		q.push(make_pair(x-1, y));
		q.push(make_pair(x, y+1));
		q.push(make_pair(x, y-1));

	}
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= m; j++) {
			if (M[i][j] == 0) W[i][j] = 0;
			else if (W[i][j] == 0) W[i][j] = -1;
		}
	W[sx][sy] = 0;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++)
			cout << W[i][j]<<" ";
		cout << endl;
	}
}
