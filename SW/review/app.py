import streamlit as st
from data import get_city_list, get_gu_list, get_town_list, get_village_list
from service import get_filtered_data, handle_preprocessing

def main():
    with st.sidebar: sidebar()
    contents()

def sidebar() :
    title =  '지역을 선택해주세요.'
    st.title(title)
    label_city_list = '시/도 선택'
    label_gu_list = '시/군/구 선택'
    label_town_list = '읍/면/동 선택'
    city_choice = st.selectbox(label_city_list, get_city_list(),
    key='city')
    gu_choice = st.selectbox(label_gu_list, get_gu_list(city_choice),
    key='gu')
    town_choice = st.selectbox(label_town_list, get_town_list(city_choice, gu_choice),
    key='town')
    vl = get_village_list(city_choice, gu_choice, town_choice)
    if vl:
        village_choice = st.selectbox(label_town_list, vl, key='village')
    else:
        st.session_state['village'] = ''

def contents():
    # st.write(get_filtered_data())
    st.write(handle_preprocessing())

if __name__ == '__main__':
    main()
    st.write('hello :)')