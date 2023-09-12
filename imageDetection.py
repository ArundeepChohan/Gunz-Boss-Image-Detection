from ultralytics import YOLO
import torch

print(f"Setup complete. Using torch {torch.__version__} ({torch.cuda.get_device_properties(0).name if torch.cuda.is_available() else 'CPU'})")
# Load a model
# model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

results = model.train(data="config.yaml", epochs=3,workers=1)  # train the model
#results = model.val()  # evaluate model performance on the validation set
results = model.predict(source="image.png", show=True, stream=True, classes=0,device='cpu' )
result = results[0]
for box in result.boxes:
    print("Object type:", box.cls)
    print("Coordinates:", box.xyxy)
    print("Probability:", box.conf)

# success = YOLO("yolov8n.pt").export(format="onnx")  # export a model to ONNX format
