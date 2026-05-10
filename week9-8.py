import matplotlib.pyplot as plt

cat = plt.imread("/content/cat.2.jpg")

plt.figure(figsize=(3,3))
plt.imshow(cat)
plt.axis('off')
plt.savefig('result.png')
plt.show()