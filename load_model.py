import openvino as ov
import os

print(f"OpenVINO version: {ov.__version__}")

model_path = "full_chain.onnx"

if not os.path.exists(model_path):
    print(f"Error: Model file '{model_path}' not found in {os.getcwd()}")
else:
    core = ov.Core()
    model = core.read_model(model_path)
    print("Model loaded successfully")
