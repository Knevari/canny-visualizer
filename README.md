# canny-visualizer

A tool to help finding the proper parameters to cv2 canny function

Execute it through the terminal using:

```
py main.py <filename>
```

Sample output:

```python
blur_image = cv2.GaussianBlur(gray_image, (3, 3), 0)
edges = cv2.Canny(blur_image, 50, 150)
```
