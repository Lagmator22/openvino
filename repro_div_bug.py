import os
import sys
import numpy as np

# 1. FORCE THE LOCAL BUILD PATH
build_bin = "/Users/lagmator22/openvino/bin/arm64/Release"
sys.path.insert(0, f"{build_bin}/python")

import openvino as ov
import openvino.opset14 as ops

print(f"\n[PYTHON] Core loaded from: {ov.__file__}")

# 2. THE DETECTOR: Use 'vmmap' to see which file is physically in RAM
def check_loaded_libs():
    print("[PYTHON] Searching RAM for loaded plugins...")
    os.system(f"vmmap {os.getpid()} | grep -i 'openvino_arm_cpu_plugin'")

# 3. SETUP MODEL
param1 = ops.parameter([1], np.float64, name="A")
param2 = ops.parameter([1], np.float64, name="B")
res = ops.divide(param1, param2)
model = ov.Model([res], [param1, param2])

core = ov.Core()
# MANUAL REGISTRATION to ensure no 'Default' system plugin is used
# core.register_plugin(f"{build_bin}/libopenvino_arm_cpu_plugin.so", "CPU")
compiled = core.compile_model(model, "CPU")

check_loaded_libs()


# 4. RUN
# We use create_infer_request() and pass a list to bypass Python binding dictionary issues
print("[PYTHON] Starting Inference Request...")
request = compiled.create_infer_request()

# Pass inputs as a list (order matches the parameters in ov.Model)
input_data = [np.array([1.0], dtype=np.float64), np.array([0.0], dtype=np.float64)]
request.infer(input_data)

# Get output (Index 0)
out = request.get_output_tensor(0).data

print(f"\nFINAL RESULT: {out}")