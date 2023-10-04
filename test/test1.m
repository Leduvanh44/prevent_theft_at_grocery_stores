target = imread('Saved Pictures/aureliansol.jpg');
image = imread('Saved Pictures/thresh_darkstar.jpg');
gray_image = rgb2gray(image);
gray_target = rgb2gray(target);
B = imhistmatch(image, gray_target);
imshowpair(B, target, 'montage')

%{
figure
subplot(1,2,1)
imhist(histeq(gray_image))
subplot(1,2,2)
imhist(histeq(gray_image, 20))
%}








