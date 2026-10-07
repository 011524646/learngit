from pathlib import Path

BASE = Path(__file__).parent

score = []
with open(BASE / 'scores.txt', 'r', encoding='utf-8') as f:
    for line in f:
        score.append(int(line))
print(score)

avg = float(sum(score) / len(score))
print(avg)

with open(BASE / 'result.txt', 'w', encoding='utf-8') as f:
    f.write("均分=" + str(avg))

try:
    with open(BASE / 'scs.txt', 'r', encoding='utf-8') as f:
        print(f.read())
except FileNotFoundError:
    print("无文件")