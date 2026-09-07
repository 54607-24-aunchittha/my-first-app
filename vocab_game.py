import streamlit as st
import time

# ---------------------------------------------------------
# 1. กำหนดค่าเริ่มต้นใน session_state (รองรับ 4 คำศัพท์)
# ---------------------------------------------------------
if 'game_started' not in st.session_state:
    st.session_state.game_started = False
if 'start_time' not in st.session_state:
    st.session_state.start_time = 0
if 'ans1_val' not in st.session_state:
    st.session_state.ans1_val = ""
if 'ans2_val' not in st.session_state:
    st.session_state.ans2_val = ""
if 'ans3_val' not in st.session_state:
    st.session_state.ans3_val = ""
if 'ans4_val' not in st.session_state:
    st.session_state.ans4_val = ""

st.title("🎮 เกมเติมคำศัพท์ภาษาอังกฤษ (Vocab Game)")

# ---------------------------------------------------------
# 2. หน้าจอก่อนเริ่มเกม (แสดงปุ่มเริ่มเล่นเกม)
# ---------------------------------------------------------
if not st.session_state.game_started:
    st.info("👋 ยินดีต้อนรับ! กดปุ่มด้านล่างเพื่อเริ่มเล่นและจับเวลา")
    if st.button("▶️ เริ่มเล่นเกม"):
        st.session_state.game_started = True
        st.session_state.start_time = time.time()  # เริ่มจับเวลา
        st.rerun()

# ---------------------------------------------------------
# 3. หน้าจอขณะเล่นเกม (โจทย์ 4 ข้อ)
# ---------------------------------------------------------
else:
    st.write("ให้นักเรียนเติมคำศัพท์ภาษาอังกฤษให้ถูกต้อง ทั้ง 4 ข้อ")

    # ข้อที่ 1: apple
    st.subheader("ข้อที่ 1: 🍎")
    ans1 = st.text_input("ผลไม้สีแดง รสชาติหวานกรอบ ภาษาอังกฤษคืออะไร?", value=st.session_state.ans1_val, key="input1")

    # ข้อที่ 2: fish
    st.subheader("ข้อที่ 2: 🐟")
    ans2 = st.text_input("สัตว์ที่อาศัยอยู่ในน้ำ ว่ายน้ำได้ ภาษาอังกฤษคืออะไร?", value=st.session_state.ans2_val, key="input2")

    # ข้อที่ 3: cat (คำศัพท์ใหม่ 1)
    st.subheader("ข้อที่ 3: 🐱")
    ans3 = st.text_input("สัตว์เลี้ยงตัวเล็ก ร้องเหมียวๆ ชอบกินปลา ภาษาอังกฤษคืออะไร?", value=st.session_state.ans3_val, key="input3")

    # ข้อที่ 4: dog (คำศัพท์ใหม่ 2)
    st.subheader("ข้อที่ 4: 🐶")
    ans4 = st.text_input("สัตว์เลี้ยงสี่ขา ซื่อสัตย์ ร้องโฮ่งๆ ภาษาอังกฤษคืออะไร?", value=st.session_state.ans4_val, key="input4")

    # อัปเดตค่าล่าสุดเข้า session_state
    st.session_state.ans1_val = ans1
    st.session_state.ans2_val = ans2
    st.session_state.ans3_val = ans3
    st.session_state.ans4_val = ans4

    # ---------------------------------------------------------
    # Popup (Dialog) สรุปผล + เวลาที่ใช้
    # ---------------------------------------------------------
    @st.dialog("📊 สรุปผลการเล่นเกม")
    def check_answers():
        # คำนวณเวลาที่ใช้ไป
        end_time = time.time()
        elapsed_time = round(end_time - st.session_state.start_time, 2)
        
        score = 0
        u_ans1 = ans1.strip().lower()
        u_ans2 = ans2.strip().lower()
        u_ans3 = ans3.strip().lower()
        u_ans4 = ans4.strip().lower()
        
        # ตรวจข้อ 1: apple
        if u_ans1 == "apple":
            score += 1
            st.success("ข้อ 1: ถูกต้อง! (Apple)")
        else:
            st.error("ข้อ 1: ผิด (เฉลย: apple)")

        # ตรวจข้อ 2: fish
        if u_ans2 == "fish":
            score += 1
            st.success("ข้อ 2: ถูกต้อง! (Fish)")
        else:
            st.error("ข้อ 2: ผิด (เฉลย: fish)")

        # ตรวจข้อ 3: cat
        if u_ans3 == "cat":
            score += 1
            st.success("ข้อ 3: ถูกต้อง! (Cat)")
        else:
            st.error("ข้อ 3: ผิด (เฉลย: cat)")

        # ตรวจข้อ 4: dog
        if u_ans4 == "dog":
            score += 1
            st.success("ข้อ 4: ถูกต้อง! (Dog)")
        else:
            st.error("ข้อ 4: ผิด (เฉลย: dog)")
            
        st.divider()
        st.subheader(f"🏆 คะแนนรวม: {score} / 4 คะแนน")
        st.info(f"⏱️ เวลาที่ใช้ไป: {elapsed_time} วินาที")
        
        if score == 4:
            st.balloons()
            st.success("🎉 สุดยอดมาก! คุณตอบถูกครบทั้ง 4 ข้อ")

    # ปุ่มส่งคำตอบ
    if st.button("ส่งคำตอบ 🚀"):
        check_answers()

    # ปุ่มเริ่มเกมใหม่
    if st.button("เริ่มเกมใหม่ 🔄"):
        st.session_state.game_started = False
        st.session_state.ans1_val = ""
        st.session_state.ans2_val = ""
        st.session_state.ans3_val = ""
        st.session_state.ans4_val = ""
        st.rerun()
st.write("นางสาวอํญชิษฐา คงโพธิ์ทอง เลขที่ 24 ม.4/4")
