target = imread('Saved Pictures/chogath_boiuoc.jpg');
image = imread('Saved Pictures/thresh_darkstar.jpg');
% matched_image = histeq(image, imhist(target));
image_red = image(:,:,1);
image_green = image(:,:,2);
image_blue = image(:,:,3);

target_red = target(:,:,1);
target_green = target(:,:,2);
target_blue = target(:,:,3);

matched_red = histeq(image_red, imhist(target_red));
matched_blue = histeq(image_blue, imhist(target_blue));
matched_green = histeq(image_green, imhist(target_green));
matched_image = cat(3, matched_red, matched_green, matched_blue);


subplot(1, 2, 1);
imshow(matched_image);
subplot(1, 2, 2);
imshow(image);