import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('C:/Users/Ruben PC/Pictures/ddd.jpg')
print(img)
imgplot = plt.imshow(img)

###############################################################################
# You can also plot any numpy array.
#
# .. _Pseudocolor:
#
# Applying pseudocolor schemes to image plots
# -------------------------------------------------
#
# Pseudocolor can be a useful tool for enhancing contrast and
# visualizing your data more easily.  This is especially useful when
# making presentations of your data using projectors - their contrast is
# typically quite poor.
#
# Pseudocolor is only relevant to single-channel, grayscale, luminosity
# images.  We currently have an RGB image.  Since R, G, and B are all
# similar (see for yourself above or in your data), we can just pick one
# channel of our data:

lum_img = img[:, :, 0]

plt.imshow(lum_img)
plt.show()
plt.imshow(lum_img, cmap="hot")
plt.show()
imgplot = plt.imshow(lum_img)
imgplot.set_cmap('nipy_spectral')
plt.show()

imgplot = plt.imshow(lum_img)
plt.colorbar()
plt.show()
plt.hist(lum_img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')


imgplot = plt.imshow(lum_img, clim=(0.0, 0.7))
plt.show()

fig = plt.figure()
a = fig.add_subplot(1, 2, 1)
imgplot = plt.imshow(lum_img)
a.set_title('Before')
plt.colorbar(ticks=[0.1, 0.3, 0.5, 0.7], orientation='horizontal')
a = fig.add_subplot(1, 2, 2)
imgplot = plt.imshow(lum_img)
imgplot.set_clim(0.0, 0.7)
a.set_title('After')
plt.colorbar(ticks=[0.1, 0.3, 0.5, 0.7], orientation='horizontal')


from PIL import Image

img = Image.open('C:/Users/Ruben PC/Pictures/ddd.jpg')
img.thumbnail((64, 64), Image.ANTIALIAS)  # resizes image in-place
imgplot = plt.imshow(img)
imgplot = plt.imshow(img, interpolation="nearest")
imgplot = plt.imshow(img, interpolation="bicubic")
plt.show()

