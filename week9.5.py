import matplotlib.pyplot as plt

blood = {'A':0,'B':0,'O':0,'AB':0}

while True:
  s = input('혈액형(A, B, O, AB) 또는 종료: ')
  if s=='종료':
    break
  elif s in blood:
    blood[s] += 1
  else:
    print('잘못 입력했습니다.')

plt.figure(figsize=(5,3))
plt.bar(blood.keys(), blood.values(), width=0.6)
plt.xlabel('blood type')
plt.ylabel('frequency')
plt.show()