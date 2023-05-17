import time
import grpc
import image_pb2
import image_pb2_grpc
import cv2

def capture_image():
    # открываем камеру
    cap = cv2.VideoCapture(0)
    print("cam opened")
    # снимочек
    ret, frame = cap.read()
    print("snapshot taken")
    # отпускаем камеру
    cap.release()
    print("cam released")
    # конвертируем в байты
    ret, image_data = cv2.imencode('.jpg', frame)
    print("print converted")
    return image_data.tobytes()

def send_image(image_data):
    # коннект к грпц серверу
    channel = grpc.insecure_channel('localhost:50051')
    stub = image_pb2_grpc.ImageServiceStub(channel)
    print("connected")
    # создаём реквест
    request = image_pb2.ImageRequest(image_data=image_data)
    print("requested")
    # отправляем реквест
    response = stub.SaveImage(request)
    print(response.status)
    print("sent")
while True:
    # снимочек
    image_data = capture_image()

    # отправляем на сервер
    send_image(image_data)
    time.sleep(10)