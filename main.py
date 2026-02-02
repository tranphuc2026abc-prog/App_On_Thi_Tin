import streamlit as st
import time

# --- CẤU HÌNH TRANG CHUYÊN NGHIỆP ---
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
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    .highlight-box {
        padding: 20px;
        border-radius: 15px;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border-left: 5px solid #007bff;
    }
    </style>
    """, unsafe_allow_html=True)

# --- KHỞI TẠO DỮ LIỆU NGƯỜI DÙNG (SESSION STATE) ---
if 'initialized' not in st.session_state:
    st.session_state.initialized = True
    st.session_state.user_name = ""
    st.session_state.progress = 0
    st.session_state.score_log = []

# --- THANH BÊN (SIDEBAR) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3449/3449605.png", width=100)
    st.title("Bảng Điều Khiển")
    if st.session_state.user_name:
        st.success(f"Chào thầy/trò: **{st.session_state.user_name}**")
        st.metric("Tiến độ ôn tập", f"{st.session_state.progress}%")
    st.divider()
    st.info("💡 Mẹo: Hãy hoàn thành phần trắc nghiệm đúng/sai trước để nắm chắc kiến thức nền tảng.")

# --- NỘI DUNG CHÍNH ---
st.title("🚀 Hệ Thống Ôn Thi Tốt Nghiệp Tin Học 2018")
st.caption("Cập nhật theo Công văn 7991/BGDĐT-GDTrH | Cố vấn chuyên môn: Thầy Khanh")

# Khu vực chào mừng
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div class="highlight-box">
        <h3>🎯 Mục tiêu học tập hôm nay là gì?</h3>
        <p>Hệ thống hỗ trợ đầy đủ 3 dạng thức câu hỏi mới nhất của Bộ Giáo dục:</p>
        <ul>
            <li><b>Phần I:</b> Trắc nghiệm 4 lựa chọn (Chọn 1 đáp án đúng).</li>
            <li><b>Phần II:</b> Trắc nghiệm Đúng/Sai (Đòi hỏi tư duy sâu).</li>
            <li><b>Phần III:</b> Trắc nghiệm Trả lời ngắn (Điền đáp án chính xác).</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("") # Khoảng cách
    
    # Nhập thông tin học sinh
    name_input = st.text_input("Nhập họ tên để hệ thống ghi nhận kết quả:", 
                               value=st.session_state.user_name,
                               placeholder="Ví dụ: Nguyễn Văn A")
    
    if name_input != st.session_state.user_name:
        st.session_state.user_name = name_input
        st.rerun()

with col2:
    # Hiển thị biểu đồ tiến độ ảo hoặc hình ảnh minh họa
    st.image("https://img.freepik.com/free-vector/learning-concept-illustration_114360-1103.jpg")

# --- DANH MỤC NHANH ---
st.subheader("🛠️ Công cụ hỗ trợ")
c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):
        st.write("📖 **Thư viện đề thi**")
        st.write("Tổng hợp hơn 500 câu hỏi bám sát 3 bộ sách (KNTT, CTST, CD).")
        if st.button("Xem danh sách đề"):
            st.toast("Đang chuyển hướng đến trang Luyện tập...")
            time.sleep(1)
            # Link này sẽ kích hoạt menu bên trái (tính năng tự động của Streamlit)

with c2:
    with st.container(border=True):
        st.write("🤖 **Trợ lý AI (Gemini)**")
        st.write("Giải đáp thắc mắc về mã nguồn Python và lý thuyết Tin học.")
        st.button("Chat với AI", key="ai_btn")

with c3:
    with st.container(border=True):
        st.write("📊 **Báo cáo kết quả**")
        st.write("Phân tích những chủ đề bạn còn yếu để tập trung ôn tập.")
        st.button("Xem thống kê", key="stat_btn")

# --- FOOTER ---
st.divider()
st.markdown(
    """
    <div style='text-align: center; color: gray;'>
        <p>© 2026 - Bản quyền thuộc về Tổ chuyên môn Toán - Tin</p>
        <p>Phụ trách nội dung: <b>Thầy Khanh</b> - Chuyên gia CNTT & Chuyển đổi số</p>
    </div>
    """, 
    unsafe_allow_html=True
)