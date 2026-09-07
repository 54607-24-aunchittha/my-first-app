# 3. ช่องรับคำตอบ (ใช้ value ผูกกับตัวแปรตรงๆ เพื่อสั่งเคลียร์ได้)
ans1 = st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    "ข้อ 2: Cats love to eat `f _ s h`. 🐟",
    value=st.session_state.ans2_val,
)

# ✏️ [พื้นที่สำหรับนักเรียน]: เพิ่มข้อ 3, 4 ตรงนี้
ans3 = st.text_input(
    "ข้อ 3: Dogs are known as man's best `f _ i e n d`. 🐶",
    value=st.session_state.ans3_val,
)
ans4 = st.text_input(
    "ข้อ 4: The sun rises in the `e _ s t`. ☀️",
    value=st.session_state.ans4_val,
)

# อัปเดตค่าล่าสุดเข้าตัวแปร
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4

st.divider()
st.write("นางสาวอํญชิษฐา คงโพธิ์ทอง เลขที่ 24 ม.4/4")
