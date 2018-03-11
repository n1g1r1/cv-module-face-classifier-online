# cv-module-face-classifier-online

Classifier that uses @quving's online CNN classifier.

## Usage

```python
classify(recognition_server_api_url, image_np)
```

- `recognition_server_api_url`: The url to the server API for recognition.
- `image_np`: The image as numpy array.

## Return

```python
return label, confidence
```

- `label`: The predicted label info for the given image as `str`.
- `confidence`: The confidence percentage as `float`.
