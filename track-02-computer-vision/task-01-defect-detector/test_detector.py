import unittest
from pathlib import Path

from detector import DEFECT_THRESHOLD, classify_image, red_pixel_ratio


SAMPLES_DIRECTORY = Path(__file__).parent


class DetectorTests(unittest.TestCase):
    def test_ok_sample(self):
        image_path = SAMPLES_DIRECTORY / "ok.png"

        self.assertLess(red_pixel_ratio(image_path), DEFECT_THRESHOLD)
        self.assertEqual(classify_image(image_path), "OK")

    def test_defect_sample(self):
        image_path = SAMPLES_DIRECTORY / "defect.png"

        self.assertGreaterEqual(red_pixel_ratio(image_path), DEFECT_THRESHOLD)
        self.assertEqual(classify_image(image_path), "DEFECT")


if __name__ == "__main__":
    unittest.main()
