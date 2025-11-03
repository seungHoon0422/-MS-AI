from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.imageanalysis.models import VisualFeatures
from PIL import Image, ImageDraw, ImageFont


COMPUTER_VISION_KEY = "<your_key>"
COMPUTER_VISION_ENDPOINT = "<your_endpoint>"

credntial = AzureKeyCredential(COMPUTER_VISION_KEY)
client = ImageAnalysisClient(endpoint=COMPUTER_VISION_ENDPOINT, 
                             credential=credntial)

def get_image_info():
    # file을 읽어오는 부분
    file_path = input("Enter the image file path: ")

    with open(file_path, "rb") as image_file:
        image_data = image_file.read()

    result = client.analyze(
        image_data=image_data,
        visual_features=[
            VisualFeatures.TAGS,
            VisualFeatures.CAPTION,
            VisualFeatures.OBJECTS
        ],
        model_version="latest"
    )

    # tags 출력 부분
    if result.tags is not None:
        print("Tags:")
        for tag in result.tags.list:
            print(f"  {tag.name} ({tag.confidence:.2f})")

    # caption 출력 부분
    if result.caption is not None:
        print("\nCaption:")
        print(f"  {result.caption.text} ({result.caption.confidence:.2f})")

    # objects 출력 부분
    image = Image.open(file_path)  # 이미지 열기
    draw = ImageDraw.Draw(image)

    if result.objects is not None:
        print("\nObjects:")
        for obj in result.objects.list:
            print(f"  {obj.tags[0].name} ({obj.tags[0].confidence:.2f}) - "
                  f"Bounding Box: {obj.bounding_box}")
            x, y, w, h = obj.bounding_box['x'], obj.bounding_box['y'], obj.bounding_box['w'], obj.bounding_box['h']
            
            draw.rectangle(((x,y),(x+w,y+h)), outline="red", width=2)
            draw.text((x,y), obj.tags[0].name, fill="red")

    image.show()  # 이미지 표시
    image.save("output.jpg")

if __name__ == "__main__":
    get_image_info()