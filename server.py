import grpc
from concurrent import futures
import image_pb2
import image_pb2_grpc
from PIL import Image
import io
#отображение может не работать как надо на безгуевских осях, но уже 3 часа ночи
class ImageService(image_pb2_grpc.ImageServiceServicer):
    def SaveImage(self, request, context):
        # сохраняем
        image_data = request.image_data
        file_path = "image.jpg"
        with open(file_path, "wb") as file:
            file.write(image_data)

        # Открываем сохранённое изображение
        image = Image.open(file_path)
        image.show()

        # ретёрним клиенту
        return image_pb2.ImageResponse(status='Image saved and displayed successfully')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    image_pb2_grpc.add_ImageServiceServicer_to_server(ImageService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
