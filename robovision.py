import torch
import json

# Model
model = torch.hub.load('./', 'custom', path='runs/train/exp5/weights/last.pt', source='local')  # local repo

# Images
img = '49.png'  # or file, PIL, OpenCV, numpy, multiple

# Inference
results = model(img)

# Results
# results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
json_results = json.loads(results.pandas().xyxy[0].to_json(orient="records"))

for result in json_results:
    print(result['name'])