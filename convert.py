from PIL import Image
import sys

def process_image(input_file, output_file):
    # 入力画像を読み込み
    image = Image.open(input_file)

    # 128×128にリサイズ（最近傍補間でピクセルアート風に）
    image = image.resize((128, 128), resample=Image.NEAREST)

    # 16色に変換（quantizeでパレット減色）
    image = image.quantize(colors=16, method=Image.FASTOCTREE)

    # 減色後の画像を保存
    image.save(output_file)
    print(f"出力画像を {output_file} に保存しました。")

    # 16色パレットを取得し、RGB.txtに保存
    palette = image.getpalette()  # 長さは通常256*3のリスト
    with open("RGB.txt", "w") as f:
        for i in range(16):
            r, g, b = palette[i*3:i*3+3]
            f.write(f"{r},{g},{b}\n")
    print("使用した16色を RGB.txt に保存しました。")

    # 画像の各ピクセルのパレットインデックスを取得し、16進数（0～F）に変換してoutputRGB.txtに保存
    width, height = image.size
    pixels = list(image.getdata())
    with open("outputRGB.txt", "w") as f:
        for y in range(height):
            # 1行分のピクセルを抽出し、各値を16進数に変換（大文字）
            row = pixels[y * width:(y + 1) * width]
            hex_row = "".join(format(pixel, "X") for pixel in row)
            f.write(hex_row + "\n")
    print("128×128の出力ピクセル情報を outputRGB.txt に保存しました。")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        input_file = "input.png"
        output_file = "output.png"
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    process_image(input_file, output_file)
