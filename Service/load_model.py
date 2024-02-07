from PIL import Image
from io import BytesIO
import time
import base64
import torch
import torchvision.transforms as transforms
from PIL import Image

import torchvision.models as models
import torch.nn as nn

from openai import OpenAI

my_key = 'my_api_key'
client = OpenAI(api_key=my_key)

def preprocessing_byte(byte_image):
    decoded = base64.b64decode(byte_image)
    IMAGE_SHAPE = (224, 224)
    user_input_image = Image.open(BytesIO(decoded)).resize(IMAGE_SHAPE)
    return user_input_image


def query_openai(result):
    result = (result[0]*100).round()
    # 작업 완료 후 결과 표시
    symptoms = f'결막염 : {result[0]}%, 유루증 : {result[1]}%, 궤양성각막질환 : {result[2]}%, 백내장 : {result[3]}%, 색소침착성각막염 : {result[4]}%, 안검종양 : {result[5]}%'
    response = client.chat.completions.create(
      model="gpt-4-0125-preview",
      messages=[
          {"role": "system", "content": "너는 아주 유능한 강아지 안구질병을 판단하는 어플이야."},
          {"role": "user", "content": f"""강아지 안구 사진으로 진단 받았을 때 각 안구 질병의 확률이 아래와 같아 : {symptoms}, 각 질병에 대한 아주 짧은 설명과 어떻게 관리하면 좋을 지 안내해줘"""}
      ]
    )

    return response.choices[0].message.content


class ViTModel(nn.Module):
    def __init__(self, num_classes):
        super(ViTModel, self).__init__()
        # 사전 훈련된 ViT 모델 로드
        self.vit = models.vit_b_16(pretrained=True)
        in_features = self.vit.heads[0].in_features
        self.vit.heads[0] = nn.Linear(in_features, num_classes)

    def forward(self, x):
        return self.vit(x)


def image_transform(x):
  transform = transforms.Compose([
      transforms.Resize((224, 224)),
      transforms.RandomHorizontalFlip(),
      transforms.RandomRotation(30),
      transforms.ColorJitter(brightness=0.5),
      transforms.RandomVerticalFlip(),
      transforms.ToTensor(),
      transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
  ])
  return transform(x)


def predict_function(image,
                     model_pth: str = 'model_inference/best_ViT.pth',
                    device: torch.device = "cpu"):
    # image = Image.open(img_path).convert("RGB")
    image = image.convert('RGB')
    image_tensor = image_transform(image).to(device)
    data = image_tensor.unsqueeze(0)
    model = ViTModel(6)
    model.load_state_dict(torch.load(model_pth))
    model.to(device)
    model.eval()
    with torch.inference_mode():
        model.eval()
        output = model(data)
    return torch.sigmoid(output)

def detect_eye_diseases(image):
    result = predict_function(model_pth,image)
    print(result)
