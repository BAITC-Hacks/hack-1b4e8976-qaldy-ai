import sys
from pathlib import Path

from PIL import Image


RED_CHANNEL_MINIMUM = 180
RED_CHANNEL_GAP = 50
DEFECT_THRESHOLD = 0.30


def red_pixel_ratio(image_path):
    with Image.open(image_path) as image:
        rgb_image = image.convert("RGB")
        pixel_bytes = rgb_image.tobytes()
        total_pixels = rgb_image.width * rgb_image.height

        red_pixels = sum(
            1
            for red, green, blue in zip(
                pixel_bytes[0::3],
                pixel_bytes[1::3],
                pixel_bytes[2::3],
            )
            if red >= RED_CHANNEL_MINIMUM
            and red - green >= RED_CHANNEL_GAP
            and red - blue >= RED_CHANNEL_GAP
        )

    return red_pixels / total_pixels


def classify_image(image_path):
    if red_pixel_ratio(image_path) >= DEFECT_THRESHOLD:
        return "DEFECT"

    return "OK"


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Использование: python detector.py <путь_к_изображению>")

    image_path = Path(sys.argv[1])
    print(classify_image(image_path))


if __name__ == "__main__":
    main()
