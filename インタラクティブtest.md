## インタラクティブ問題のローカルテスト

### 基本方針

- アルゴリズム中で直接 `cout << "?"` しない
- `query()` と `answer()` を作る
- `DEBUG` 時だけ自作ジャッジに切り替える

### query / answer

```cpp
#ifdef DEBUG
vector<ll> hidden;
ll query_count;
ll final_answer;
#endif

bool query(ll i, ll l, ll r){
#ifdef DEBUG
  query_count++;
  return l <= hidden[i] && hidden[i] <= r;
#else
  cout << "? " << i+1 << " " << l << " " << r << endl;
  string res;
  cin >> res;
  return res == "Yes";
#endif
}

void answer(ll x){
#ifdef DEBUG
  final_answer = x;
#else
  cout << "! " << x << endl;
#endif
}
```

### solve 側

```cpp
void solve(){
  // 普通にアルゴリズムを書く

  bool res = query(i, l, r);

  // ...

  answer(ans);
}
```

### DEBUG 側の test

```cpp
void test(){
  rep(tc,100000){
    ll n = rnd(1,10);

    hidden.resize(n);
    rep(i,n) hidden[i] = rnd(-100,100);

    query_count = 0;

    // 最初にジャッジから与えられる入力
    string input = to_string(n) + '\n';
    run(solve, input);

    ll correct = *max_element(all(hidden));

    if(final_answer != correct){
      cerr << "hidden = " << hidden << endl;
      cerr << "correct = " << correct << endl;
      cerr << "actual = " << final_answer << endl;
      return;
    }

    if(query_count > 5000){
      cerr << "query limit exceeded" << endl;
      return;
    }
  }
}
```

### 覚えておくこと

- `run()`：最初にジャッジから与えられる入力を再現
- `query()`：その後のやり取りを自作ジャッジに切り替える
- `answer()`：最終回答を記録して正解と比較
- `query_count`：質問回数制限の確認
- 正解を直接計算できるなら `naive()` は不要
- 適応的ジャッジなら `query()` 内で質問履歴に応じて返答を決める
- インタラクティブでは `endl` を使って flush する