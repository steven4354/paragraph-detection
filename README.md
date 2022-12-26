Test using OpenCV to group together texts into paragraphs from research papers

# Running

```bash
docker build -t bounding-boxes .
docker run -it bounding-boxes
docker ps
# plug the above id into below
# docker cp <id>:/app/image_with_boxes.jpg .
docker cp 10b2438d4b4f:/app/image_with_boxes.jpg .
```