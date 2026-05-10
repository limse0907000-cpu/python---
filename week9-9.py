import matplotlib.pyplot as plt

cat = plt.imread('cat2.jpg')
dog = plt.imread('dog2.jpg')

plt.figure(figsize=(5,3))

plt.subplot(1,2,1)
plt.imshow(cat)
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(dog)
plt.axis('off')

plt.show()