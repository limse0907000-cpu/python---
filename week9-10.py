import matplotlib.pyplot as plt

cat = plt.imread('cat2.jpg)')
dog = plt.imread('dog2.jpg')
imgs = [cat,dog]

plt.figure(figsize=(5,3))
for i in range(len(imgs)):
    plt.subplot(1,2,i+1)
    plt.imshow(imgs[i])
    plt.axis('off')
plt.show()