<p align="center"><img src="https://github.com/jinucho/DL_for_pets/assets/133849027/45f7cab1-7fdb-4acb-a850-863165de26c3" width="300" height="300"/>




# 딥러닝 프로젝트(강아지 안구 질병 예측)</br>Dog eye disease prediction
- Team : 숨참고딥다이브

## :sunny:팀구성 
  * 👥팀원 : 김유진, 송영달, 이수현, 이호, 조진우
  * :clock1:시작일 : 2024.01.29(월)
  * ⏰목표일 : 2024.02.08(목)

## 목차(INDEX)
&emsp;&ensp;Ⅰ. 🏁프로젝트 목적</br>
&emsp;&emsp;&emsp;- 반려견 안구 사진을 통한 질병 예측 서비스 개발</br>
&emsp;&ensp;Ⅱ. 📑데이터의 구성확인</br>
&emsp;&emsp;&emsp;1.- 출처 : [AIHub](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=562)</br>
&emsp;&emsp;&emsp;2.- 데이터파일 구성  : 이미지 & json</br>
&emsp;&ensp;Ⅲ. 📑원본 데이터 분석</br>
&emsp;&emsp;&emsp;1. 질병 종류 확인</br>
&emsp;&emsp;&emsp; 결막염 / 궤양성각막질환 / 백내장 / 비궤양성각막질환 / 색소침착성각막염 / 안검내반증 / 안검염 / 안검종양 / 유루증 / 핵경화
&emsp;&emsp;&emsp;2. 학습에 사용할 질병 별 이미지 확인</br>
&emsp;&emsp;&emsp; <img src="https://github.com/jinucho/DL_for_pets/assets/133849027/1966441a-11e7-4aa0-ba07-0b45a9f2b77b" width="400">
&emsp;&emsp;&emsp;3. json file 형식 확인</br>
&emsp;&ensp;Ⅳ. 📋데이터셋 구성</br>
&emsp;&emsp;&emsp; 이미지 및 json의 필요한 label만 추출하여 데이터셋 구성</br>
&emsp;&ensp;Ⅴ. ✔학습 모델과 모델 성능평가</br>
&emsp;&emsp;&emsp; AlexNet / VGG19 / ViT / ResNet50 / DenseNet201 / GoogleNet</br>
&emsp;&emsp;&emsp;1. AlexNet</br>
&emsp;&emsp;&emsp; <img src="https://github.com/jinucho/DL_for_pets/assets/133849027/c341d4d9-101c-4a6d-bf0e-2da9afe14cb7" width="400"> <img src="https://github.com/jinucho/DL_for_pets/assets/133849027/e8d27982-1a32-4b8a-92df-c3145bbdc913" width="400"></br>
&emsp;&emsp;&emsp;2. VGG19</br>
&emsp;&emsp;&emsp; <img src="https://github.com/jinucho/DL_for_pets/assets/133849027/bb09327a-64cb-47d2-8894-a9941f59d641" width="400"> <img src="https://github.com/jinucho/DL_for_pets/assets/133849027/5e28eb7b-28ec-432a-9090-d536a3225a79" width="400"></br>
&emsp;&emsp;&emsp;3. ViT</br>
&emsp;&emsp;&emsp; <img src="https://github.com/jinucho/DL_for_pets/assets/133849027/e0b0e686-062c-455a-86ea-8c9f71bc344a" width="400"> <img src="https://github.com/jinucho/DL_for_pets/assets/133849027/fd7f9dec-b5b8-4053-affc-d92ea7adcfda" width="400"></br>
&emsp;&emsp;&emsp;4. ResNet50</br>
&emsp;&emsp;&emsp; <img src="https://github.com/jinucho/DL_for_pets/assets/133849027/e0de7335-f4af-4582-8933-66e353598870" width="400"> <img src="https://github.com/jinucho/DL_for_pets/assets/133849027/ffac6f22-92f6-4163-85c5-65bf7e3e18db" width="400"></br>
&emsp;&emsp;&emsp;5. DenseNet201</br>
&emsp;&emsp;&emsp; <img src="https://github.com/jinucho/DL_for_pets/assets/133849027/d8204638-e11b-44f6-afc8-a1394cc290fd" width="400"> <img src="https://github.com/jinucho/DL_for_pets/assets/133849027/9d0ca8b3-f9a1-42d5-ad4c-5ea4afd5ecb6" width="400"></br>
&emsp;&emsp;&emsp;6. GoogleNet</br>
&emsp;&emsp;&emsp; <img src="https://github.com/jinucho/DL_for_pets/assets/133849027/2e984a82-81d9-4a32-8f58-2b26be0b4d4c" width="400"> <img src="https://github.com/jinucho/DL_for_pets/assets/133849027/17d900b9-944f-407f-8be3-6765cff0a0a1" width="400"></br>
&emsp;&emsp;&emsp; Model 성능 비교</br>
&emsp;&emsp;&emsp; <img src="https://github.com/jinucho/DL_for_pets/assets/133849027/b86f68c2-5644-4695-9894-9224635b1cbc" width="400"> <img src="https://github.com/jinucho/DL_for_pets/assets/133849027/3036be51-e685-44f0-bc16-052c4690769e" width="400"></br>

&emsp;&ensp;VI. 📑Streamlit 서비스</br>
&emsp;&emsp;&emsp; <img src="https://github.com/jinucho/DL_for_pets/assets/133849027/4c5eb98c-a4f6-47e0-b51e-2a673d03c3bd" width="700"></br>



&emsp;&ensp;Ⅵ. 🚨사용기술</br>
&emsp;&emsp;&emsp; Python / Pytorch / pandas / streamlit / flask / etc...</br>
