import subprocess
import random
import sys
import os


if len(sys.argv) < 2:
    print("Usage: python3 interactive_judge.py code.cpp", file=sys.stderr)
    sys.exit(1)

source_file = sys.argv[1]
exe_file = "./a.out"

# g++ -std=c++23 -g -fsanitize=address -Wall -Wextra -I . code.cpp

compile_cmd = [
    "g++",
    "-std=c++23",
    "-g",
    "-fsanitize=address",
    "-Wall",
    "-Wextra",
    "-I",
    ".",
    source_file,
    "-o",
    exe_file,
]


print("[judge] compiling...", file=sys.stderr)

res = subprocess.run(
    compile_cmd,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
)

if res.returncode != 0:
    print("[judge] compile error", file=sys.stderr)
    print(res.stderr, file=sys.stderr)
    sys.exit(1)

print("[judge] compile succeeded", file=sys.stderr)


def output_info(X,seed): #だめなケースを出力。適宜変更
    print(f"X = {X},seed ={seed}", file=sys.stderr)

# 初期入力が必要なら送る
# send(str(N))

for seed in range(10000):
    random.seed(seed) # 再現性担保 同じシードでrandom.randint()すると同じのが出てくる

    N = 10000
    X = random.randint(1, N)
    QUERY_LIMIT = 64
    q =0

    proc = subprocess.Popen(
        [exe_file],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,
    )

    def send(s):
        print(f"[judge -> solver] {s}", file=sys.stderr)
        proc.stdin.write(s + "\n")
        proc.stdin.flush()

    def recv():
        line = proc.stdout.readline()
        if line == "":
            raise RuntimeError("solver terminated unexpectedly")
        line = line.strip()
        print(f"[solver -> judge] {line}", file=sys.stderr)
        return line

    SX = str(X)
    while True:
        line = recv()
        parts = line.split()

        if len(parts) == 2 and parts[0] == "?":
            q += 1
            if q > QUERY_LIMIT:
                output_info(X,seed)
                print("WA: query limit exceeded", file=sys.stderr)
                proc.kill()
                exit(0)
                break

            m = int(parts[1])

            # if not (1 <= m <= N):
            #     print("WA: invalid query", file=sys.stderr)
            #     proc.kill()
            #     break
            sm = str(m)


            if m <= X and sm <= SX:
                send("Y")
            elif m > X and sm > SX:
                send("Y")
            else:
                send("N")

        elif len(parts) == 2 and parts[0] == "!":
            ans = int(parts[1])
            if ans == X:
                print(f"AC: X = {X}, queries = {q}", file=sys.stderr)
            else:
                print(f"WA: expected {X}, got {ans}", file=sys.stderr)
                proc.kill()
                exit(0)
            break

        else:
            print(f"WA: invalid output: {line}", file=sys.stderr)
            proc.kill()
            exit(0)
            break