Test using OpenCV to group together texts into paragraphs from research papers

# Running

```
docker build -t bounding-boxes .
docker run -it bounding-boxes
docker cp eb286b8089dc:/app/image_with_boxes.jpg .
```