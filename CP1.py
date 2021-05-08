import numpy as np
import matplotlib.pyplot as plt

# 変数の初期化、xは割合、rは各々の期待収益率、SDは各々の標準偏差、CORRは2銘柄株式の期待収益率の相関
x1 = []
x2 = []
R1 = 0.26
R2 = 0.06
SD1 = 0.50
SD2 = 0.25
CORR = 0

for i in range(0,101):
  x1.append(0.01 * i)
  x2.append(1.00 - 0.01*i)
# print(x1, x2)

# 期待収益率の計算
EX_list = []
for i in range(0, 101):
  r = x1[i] * R1 + x2[i] * R2
  EX_list.append(r)
# print(EX_list)

# ボラティリティの計算
VAR_list = []
VOL_list = []
for i in range(0, 101):
  v = (x1[i] **2) * (SD1 ** 2) + (x2[i] ** 2) * (SD2 ** 2) + 2 * x1[i] * x2[i] * CORR * SD1 * SD2
  VAR_list.append(v)
  VOL = v ** 0.5
  VOL_list.append(VOL)
# print(VAR_list)

#グラフを描画
plt.title("Efficient portfolio consisting of two stocks")
plt.xlabel("volatility")
plt.ylabel("Expected rate of return")
plt.xlim(0,0.60)
plt.ylim(0,0.3)
plt.grid(True)
plt.scatter(VOL_list, EX_list, s = 10, c = "green")
plt.show()
