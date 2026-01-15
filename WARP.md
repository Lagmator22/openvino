# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Commonly Used Commands

### Build

To build the project on macOS, first, create a build directory and run CMake to configure the project. Then, build the project using the following commands:

```sh
mkdir build && cd build
cmake -G "Ninja Multi-Config" -DENABLE_SYSTEM_PUGIXML=ON -DENABLE_SYSTEM_SNAPPY=ON -DENABLE_SYSTEM_PROTOBUF=ON ..
cmake --build . --config Release --parallel $(sysctl -n hw.ncpu)
```

### Run Tests

To run the tests, execute the test binaries from the artifacts directory. For example:

```sh
<source dir>/bin/intel64/Release/ieFuncTests
```

## Code Architecture

The OpenVINO toolkit is a C++ project that uses CMake for its build system. The high-level directory structure is as follows:

*   `src`: Contains the core source code of OpenVINO.
*   `tests`: Contains the tests for the project.
*   `samples`: Contains sample applications that demonstrate how to use OpenVINO.
*   `docs`: Contains the documentation for the project.
*   `tools`: Contains various tools for working with OpenVINO.
*   `thirdparty`: Contains third-party dependencies.

The project is organized into several components, including:

*   **Frontends**: Responsible for importing models from different frameworks like ONNX, TensorFlow, and PyTorch.
*   **Plugins**: Provide support for different hardware devices like CPU, GPU, and NPU.
*   **Core**: The core of the OpenVINO runtime.
*   **APIs**: Provides APIs for different programming languages like C++, Python, and C.
