Scale_display_dataset - 
==============================

The dataset includes 468 images.
LED-Display are annotated in YOLOv8 format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 512x512 (Stretch)

The following augmentation was applied to create 5 versions of each source image:
* Equal probability of the following 90-degree rotations: none, clockwise, counter-clockwise, upside-down

This repo contains a few examples of weighing scale dataset, given in folders */images* and it's corresponding labels in */labels*.