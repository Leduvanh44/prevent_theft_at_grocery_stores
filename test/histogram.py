import cv2
from matplotlib import pyplot as plt
from skimage import exposure, io
# target = io.imread('Saved Pictures/chogath_boiuoc.jpg')
target = cv2.imread('Saved Pictures/AurelionSol_0.jpg')
target = cv2.cvtColor(target, cv2.COLOR_RGB2BGR)
image = cv2.imread('Saved Pictures/silco.jpeg')
image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
matched = exposure.match_histograms(image, target, multichannel=True)
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(target)
plt.title('Grayscale Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(image)
plt.title('Reference Image')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(matched)
plt.title('Matched Image')
plt.axis('off')

plt.show()
# matched_image = exposure.match_histograms(image, target)

# plt.figure(figsize=(12, 4))

# plt.subplot(1, 3, 1)
# plt.imshow(target, cmap='gray')
# plt.title('Grayscale Image')
# plt.axis('off')

# plt.subplot(1, 3, 2)
# plt.imshow(image, cmap='gray')
# plt.title('Reference Image')
# plt.axis('off')

# plt.subplot(1, 3, 3)
# plt.imshow(matched_image, cmap='gray')
# plt.title('Matched Image')
# plt.axis('off')

# plt.show()

# # equalized_image = cv2.equalizeHist(image)

# hist_original = cv2.calcHist([image], [0], None, [256], [0, 256])
# hist_target = cv2.calcHist([target], [0], None, [256], [0, 256])
# hist_matchimg, _ = exposure.histogram(matched_image)


# plt.figure(figsize=(12, 0))
# plt.subplot(1, 3, 1)
# plt.plot(hist_original)
# plt.title('Histogram of Original Image')
# plt.xlabel('Pixel Value')
# plt.ylabel('Frequency')

# plt.subplot(1, 3, 2)
# plt.plot(hist_target)
# plt.title('Histogram of Taget Image')
# plt.xlabel('Pixel Value')
# plt.ylabel('Frequency')

# plt.subplot(1, 3, 3)
# plt.plot(hist_matchimg)
# plt.title('Histogram of MAtch Image')
# plt.xlabel('Pixel Value')
# plt.ylabel('Frequency')
# plt.show()