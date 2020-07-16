import cv2
import argparse

class EdgesVisualizer:
    def __init__(self, image, ksize=3, low_threshold=50, high_threshold=150):
        self._img = image
        self._ksize = ksize
        self._low_threshold = low_threshold
        self._high_threshold = high_threshold

        def onChangeLowThreshold(value):
            self._low_threshold = value
            self._render()

        def onChangeHighThreshold(value):
            self._high_threshold = value
            self._render()

        def onChangeKernelSize(value):
            self._ksize = value
            self._ksize += self._ksize + 1 % 2
            self._render()

        cv2.namedWindow('Edges')

        cv2.createTrackbar('Low Threshold', 'Edges', self._low_threshold, 255, onChangeLowThreshold)
        cv2.createTrackbar('High Threshold', 'Edges', self._high_threshold, 255, onChangeHighThreshold)
        cv2.createTrackbar('Kernel Size (For Gaussian Blur)', 'Edges', self._ksize, 15, onChangeKernelSize)

        self._render()

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def getLowThreshold(self):
        return self._low_threshold

    def getHighThreshold(self):
        return self._high_threshold

    def getKernelSize(self):
        return self._ksize

    def _render(self):
        self._blurred_img = cv2.GaussianBlur(self._img, (self._ksize, self._ksize), 0)
        self._edges = cv2.Canny(self._blurred_img, self._low_threshold, self._high_threshold)
        cv2.imshow('Edges', self._edges)


def main():
    parser = argparse.ArgumentParser(description='Receive a filename')
    parser.add_argument('filename')

    args = parser.parse_args()

    image = cv2.imread(args.filename, cv2.IMREAD_GRAYSCALE)
    edges = EdgesVisualizer(image)

    ksize          = edges.getKernelSize()
    low_threshold  = edges.getLowThreshold()
    high_threshold = edges.getHighThreshold()

    print("cv2.GaussianBlur(gray_image, (%d, %d), 0)" % (ksize, ksize))
    print("cv2.Canny(gray_image, %d, %d)" % (low_threshold, high_threshold))


if __name__ == '__main__':
    main()
