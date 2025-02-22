# EXIF orientations

JPEG images can be rotated (and mirrored) without having to reencode raster data, and thus without incurring additional quality loss, simply using EXIF tags.

Starting from this image:

![a sample image](base-exif-image.jpg)

`Exif.Image.Orientation` values 1 - 8:

![various values in increasing order](exif-orientations.jpg)

![various values in without mirroring then with mirorring](exif-orientations-2.jpg)

In the following table, angles are in degrees, counterclockwise.

| `Exif.Image.Orientation` | Angle | Mirrored |
|--------------------------|-------|----------|
| 1                        | 0     |          |
| 2                        | 0     | yes      |
| 3                        | 180   |          |
| 4                        | 180   | yes      |
| 5                        | 270   | yes      |
| 6                        | 270   |          |
| 7                        | 90    | yes      |
| 8                        | 90    |          |
