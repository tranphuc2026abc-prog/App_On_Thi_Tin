import streamlit as st
import time

# --- CẤU HÌNH TRANG (Bắt buộc dòng đầu) ---
st.set_page_config(
    page_title="Hệ thống Ôn thi Tin học 2018",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- PHONG CÁCH GIAO DIỆN (CSS) ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    /* Tùy chỉnh nút bấm cho đẹp hơn */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        font-weight: bold;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.02); /* Hiệu ứng phóng to nhẹ khi di chuột */
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .highlight-box {
        padding: 25px;
        border-radius: 15px;
        background-color: white;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        border-left: 6px solid #007bff;
    }
    </style>
    """, unsafe_allow_html=True)

# --- KHỞI TẠO SESSION STATE (Lưu dữ liệu học sinh) ---
if 'initialized' not in st.session_state:
    st.session_state.initialized = True
    st.session_state.user_name = ""
    st.session_state.progress = 0

# --- THANH BÊN (SIDEBAR) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3449/3449605.png", width=80)
    st.title("Bảng Điều Khiển")
    
    if st.session_state.user_name:
        st.success(f"👤 Học sinh: **{st.session_state.user_name}**")
        # Thanh tiến độ giả lập
        st.write("Tiến độ ôn tập:")
        st.progress(st.session_state.progress)
    else:
        st.warning("Chưa nhập tên học sinh")
        
    st.divider()
    st.info("💡 **Mẹo ôn thi:**\nPhần trắc nghiệm Đúng/Sai yêu cầu tư duy tổng hợp. Hãy đọc kỹ từng ý a, b, c, d.")

# --- NỘI DUNG CHÍNH ---
st.title("🚀 Hệ Thống Ôn Thi Tốt Nghiệp Tin Học 2018")
st.caption(f"Cập nhật theo Công văn 7991/BGDĐT-GDTrH | Phụ trách: Thầy Khanh (Tổ trưởng chuyên môn)")

# 1. Khu vực Chào mừng & Nhập tên
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div class="highlight-box">
        <h3>🎯 Mục tiêu hôm nay</h3>
        <p>Hệ thống cung cấp đầy đủ 3 dạng bài thi theo quy chế mới:</p>
        <ul>
            <li>✅ <b>Phần I:</b> Trắc nghiệm nhiều lựa chọn.</li>
            <li>✅ <b>Phần II:</b> Trắc nghiệm Đúng/Sai (Điểm liệt nếu khoanh bừa!).</li>
            <li>✅ <b>Phần III:</b> Trắc nghiệm Trả lời ngắn.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("") # Tạo khoảng trống
    
    # Ô nhập tên có tính năng lưu lại
    name_input = st.text_input("Nhập họ và tên của em để bắt đầu:", 
                               value=st.session_state.user_name,
                               placeholder="Ví dụ: Lê Văn Tình...")
    
    if name_input and name_input != st.session_state.user_name:
        st.session_state.user_name = name_input
        st.toast(f"Đã lưu tên: {name_input}", icon="✅")
        time.sleep(1)
        st.rerun()

with col2:
    st.image("https://img.freepik.com/free-vector/online-test-concept-illustration_114360-5536.jpg", caption="Ôn tập mọi lúc, mọi nơi")

# 2. Khu vực Chức năng (Các nút bấm điều hướng)
st.divider()
st.subheader("🛠️ Chọn chức năng ôn tập")

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):
        st.subheader("📖 Thư viện đề")
        st.write("Ngân hàng câu hỏi trắc nghiệm bám sát 3 bộ sách giáo khoa.")
        
        # NÚT BẤM CHUYỂN TRANG
        if st.button("Luyện tập ngay ➜", type="primary"):
            # Lệnh này sẽ chuyển hướng sang file 1_Luyen_Tap.py
            try:
                st.switch_page("pages/1_Luyen_Tap.py")
            except Exception as e:
                st.error("⚠️ Chưa tìm thấy trang Luyện tập. Thầy hãy tạo file 'pages/1_Luyen_Tap.py' nhé!")

with c2:
    with st.container(border=True):
        st.subheader("⏱️ Thi thử")
        st.write("Làm bài thi hoàn chỉnh có bấm giờ và tính điểm theo quy chế.")
        
        if st.button("Vào phòng thi ➜"):
            try:
                st.switch_page("pages/2_Thi_Thu.py") 
            except:
                st.warning("⚠️ Chức năng đang phát triển")

with c3:
    with st.container(border=True):
        st.subheader("🤖 Trợ lý AI")
        st.write("Hỏi đáp kiến thức Tin học và hỗ trợ sửa lỗi lập trình Python.")
        
        if st.button("Chat với Gemini ➜"):
            try:
                st.switch_page("pages/3_Tro_Ly_AI.py")
            except:
                st.warning("⚠️ Chức năng đang phát triển")

# --- FOOTER ---
st.divider()
st.markdown(
    """
    <div style='text-align: center; color: #6c757d; font-size: 0.9em;'>
        <p>© 2026 Bản quyền thuộc về <b>Thầy Khanh</b></p>
        <p><i>Ứng dụng hỗ trợ chuyển đổi số trong dạy và học môn Tin học</i></p>
    </div>
    """, 
    unsafe_allow_html=True
)