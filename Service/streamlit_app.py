import streamlit as st
import requests
import base64
from PIL import Image

if __name__ == '__main__':
    try:
        # 첫 번째 페이지 - 반려견 정보 입력
        st.set_page_config(layout="wide", page_title="반려견 안구질환 진단 PY1")

        # 사이드바에 페이지 선택 옵션 추가
        with st.sidebar:
            st.write("## 페이지 네비게이션")
            selected_page = st.radio("페이지 선택", ["반려견 정보 입력", "반려견 안구 사진 진단"])

        # 페이지 1: 반려견 정보 입력

        # 페이지 1: 반려견 정보 입력
        if selected_page == "반려견 정보 입력":
            st.write("## 우리 강아지 눈 건강 확인")
            st.markdown("<h2 style='color: blue; font-size: 35px;'>반려견 정보를 입력하세요</h2>", unsafe_allow_html=True)

            st.title("반려견 정보 입력")
            # 기존 입력값을 불러옵니다 (있을 경우)
            pet_name = st.text_input("반려견 이름", value=st.session_state.get('pet_name', ''))
            pet_age = st.number_input("반려견 나이", 0, 30, value=st.session_state.get('pet_age', 0))
            pet_breed = st.text_input("반려견 품종", value=st.session_state.get('pet_breed', ''))
            pet_weight = st.number_input("반려견 몸무게 (kg)", 0.0, 100.0, value=st.session_state.get('pet_weight', 0.0))

            # 저장 버튼
            if st.button("저장"):
                st.session_state.pet_name = pet_name
                st.session_state.pet_age = pet_age
                st.session_state.pet_breed = pet_breed
                st.session_state.pet_weight = pet_weight
                st.session_state.current_page = 'page2'
                st.success("반려견 정보가 저장되었습니다. 다음 페이지로 이동합니다.")

        # 페이지 2: 반려견 안구 사진 진단
        elif selected_page == "반려견 안구 사진 진단":
            st.title("우리 강아지 눈 건강 확인")
            st.write("우리 강아지 사진으로 가능한 안구 질환을 감지해보세요")

            MAX_FILE_SIZE = 5 * 1024 * 1024

            # my_upload = st.file_uploader("사진 업로드", type=["png", "jpg", "jpeg"])
            my_upload = st.file_uploader("사진 업로드", type=["png", "jpg"])

            if my_upload is not None:
                if my_upload.size > MAX_FILE_SIZE:
                    st.error("사진 크기는 5MB 이하로 설정하세요.")
                else:
                    # image = Image.open(my_upload)
                    # st.image(image, use_column_width=True)
                    st.image(my_upload, width=250)

                    # with st.expander("우리 강아지 안구질환 진단하기"):
                    button_clicked = st.button("진단 시작")

                    if button_clicked:
                        with st.spinner('진단을 수행 중입니다...'):
                            img_bytes= my_upload.read()
                            encoded = base64.b64encode(img_bytes).decode('utf-8') #byte를 문자열로 변환
                            url = 'http://127.0.0.1:5003/predict'
                            data = {"image_data":encoded}
                            response = requests.post(url,data=data)
                            if response.ok:
                                st.write(f'분석 결과:{response.json()}')
                            else:
                                st.write('서버 오류로 인해 분석을 완료할 수 없습니다')
    

    except Exception as e:
        st.write(f"오류가 발생하였습니다:{str(e)}")