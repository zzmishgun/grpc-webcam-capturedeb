## Project Description
This project consists of a client-server system where the client sends a camera snapshot to the server using gRPC. The server saves the image and displays it. The client captures an image using the computer's camera, converts it to bytes, and sends it to the server. The server receives the image, saves it to disk, opens it, and displays it using the PIL library.
upd:added server docker file with propper depences

## Dependencies
The following dependencies are required to run the project:

- Python 3.x
- grpcio
- grpcio-tools
- Pillow (PIL)
- OpenCV (cv2)

## Installation and Setup
1. Clone the repository to your local machine:

   ```
   git clone https://github.com/zzmishgun/grpc-webcam-capturedeb
   ```

2. Change to the project directory:

   ```
   cd grpc-webcam-capturedeb
   ```

3. Install the required Python packages. You can use pip, the package installer for Python:

   ```
   pip install grpcio grpcio-tools Pillow opencv-python
   ```

## Compiling Protocol Buffers
The client and server use protocol buffers for communication. To generate the necessary gRPC code from the protocol buffer definition, follow these steps:

1. Navigate to the project directory:

   ```
   cd grpc-webcam-capturedeb
   ```

2. Run the following command to compile the `.proto` file:

   ```
   python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. image.proto
   ```

   This command uses the `grpc_tools.protoc` module to compile the `image.proto` file and generate the corresponding Python files.

## Running the Server
To run the server, execute the following command:

```
python server.py
```

The server will start running on `localhost` at port `50051`.

## Running the Client
To run the client, execute the following command:

```
python client.py
```

The client will capture an image from the camera, convert it to bytes, and send it to the server. The server will save the image, display it using the PIL library, and send a response back to the client.

## Additional Notes
- Make sure the server is running before executing the client.
- The client sends an image to the server every 10 seconds in an infinite loop. You can modify the delay in the `while True` loop in `client.py` according to your requirements.
