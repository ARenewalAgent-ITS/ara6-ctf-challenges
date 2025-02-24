# TL;DR
Reverse output gdal2tiles using tilemapresource.xml

# Solve
Diberikan beberapa file:
```original-modified.pgw```: file yang berisi informasi spasial untuk gambar raster.
```original-modified.png.aux.xml```: file metadata dari ArcGIS untuk menyimpan informasi tambahan tentang gambar raster.
```original-modified.png```: file gambar raster.
```original-modified.png.ovr```: file data piramida untuk gambar raster.
```original-modified.png.xml```: file XML yang berisi metadata untuk gambar raster.

Perhatikan pada folder tile-output. Di sana terdapat file tilemapresource.xml dan beberapa dir. Jadi, folder tile-output adalah output dari command 'gdal2tiles -z 0-5 -w leaflet original.tif tile-output'.

Bagaimana cara user bisa tau? `https://www.youtube.com/watch?v=31J3pPCStKw`, user bisa searching `geospasial tool`, `raster tool`,  `tool like arcgis`, dll.

gdal2tiles adalah tools untuk mengubah file .tif menjadi tile layer (tile-output).

So, konversi ```gdal_translate -of GTiff original-modified.png original-modified.tif```

User perlu mengecek informasi mengenai file .tif ini, ```gdalinfo original-modified.tif```
Problem: 
```
Corner Coordinates:
Upper Left  (  -0.5000000,   0.5000000) (  0d30' 0.00"W,  0d30' 0.00"N)
Lower Left  (      -0.500,   -1956.500) (  0d30' 0.00"W,Invalid angle)
Upper Right (    2928.500,       0.500) (Invalid angle,  0d30' 0.00"N)
Lower Right (    2928.500,   -1956.500) (Invalid angle,Invalid angle)
Center      (    1464.000,    -978.000) (Invalid angle,Invalid angle)
```

Terdapat invalid angle, inilah yang menjadi alasan kenapa file '.tif' tidak bisa dibuka via ArcGis / Tile Layer.

Kita bisa repair menggunakan data corner coordinates dari original.tif yang bisa didapatkan melalui tilemapresource.xml:
```<BoundingBox minx="8.49940967600014" miny="44.68120028221342" maxx="11.42827153744795" maxy="46.63789675900006"/>```

```gdal_edit -a_ullr 8.49940967600014 46.63789675900006 11.42827153744795 44.68120028221342 original-modified.tif```

Cek gdalinfo, maka invalid angle akan hilang dan file repaired. Tinggal buka .tif menggunakan ArcGis atau konversi .tif ke tile layer. Maka terlihat raster tersebut mengarah ke `lentate sul seveso`.
