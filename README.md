# PixelConverter
森羅万象CPU上で表示するための画像を作成するツール


cd PixelConverter/
docker build -t pixelart-converter .
docker run --rm -v "$(pwd)":/app pixelart-converter
