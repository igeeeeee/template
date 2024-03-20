#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (long long i = 0; i < (long long)(n); i++)
#define rrep(i,start,end) for (long long i = start;i >= (long long)(end);i--)
#define repn(i,end) for(long long i = 0; i <= (long long)(end); i++)
#define reps(i,start,end) for(long long i = start; i < (long long)(end); i++)
#define repsn(i,start,end) for(long long i = start; i <= (long long)(end); i++)
#define each(p,a) for(auto &p:a)
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef vector<long long> vll;
typedef vector<vector<long long>> vvll;
typedef map<long long , long long> mpll;
typedef pair<long long ,long long> pll;
typedef tuple<long long , long long , long long> tpl3;
#define LL(...) ll __VA_ARGS__; input(__VA_ARGS__)
#define LD(...) ld __VA_ARGS__; input(__VA_ARGS__)
#define Str(...) string __VA_ARGS__; input(__VA_ARGS__)
#define Ch(...) char __VA_ARGS__; input(__VA_ARGS__)
#define all(a)  (a).begin(),(a).end()
#define UNIQUE(v) v.erase( unique(v.begin(), v.end()), v.end() );
// << std::fixed << std::setprecision(10)
const ll INF = 1LL << 60;
 
inline ll popcnt(ull a){ return __builtin_popcountll(a); }
template<class T> bool chmin(T& a, T b){if(a > b){a = b;return true;}return false;}
template<class T> bool chmax(T& a, T b){if(a < b){a = b;return true;}return false;}
template<class... T>void input(T&... a){(cin >> ... >> a);}
//grid探索用
vector<ll> _ta = {0,0,1,-1,1,1,-1,-1};
vector<ll> _yo = {1,-1,0,0,1,-1,1,-1};
	
ll lpow(ll x,ll n){ll ans = 1;while(n >0){if(n & 1)ans *= x;x *= x;n >>= 1;}return ans;}
ll Modlpow(ll x,ll n,ll m){ll ans = 1;ll a = x;while(n >0){if(n & 1){ans *= a;ans%= m;}a *= a;a %= m;n >>= 1;}return ans;} 

int main(){
	ios::sync_with_stdio(false);cin.tie(nullptr);
	fstream f;
	f.open("../input.txt");
	vector<string> words;
	while(!f.eof()){
		// cout << "here" << endl;
		string s;
		getline(f,s);
		words.push_back(s);
	}
	ofstream o;
	o.open("../output.txt");
	each(p,words){
		o <<"\""  << p << "\"," << endl;
	}

}