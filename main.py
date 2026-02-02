import streamlit as st

# 1. Cấu hình trang (Phải đặt ở dòng đầu tiên của code)
st.set_page_config(
    page_title="Ôn thi tốt nghiệp Tin học 2018",
    page_icon="💻",
    layout="wide"
)

# 2. Khởi tạo Session State (Để lưu dữ liệu khi chuyển trang)
# Đây là kỹ thuật quan trọng giúp điểm số không bị mất khi học sinh bấm qua lại các menu
if 'ten_hoc_sinh' not in st.session_state:
    st.session_state.ten_hoc_sinh = ""
if 'diem_tong' not in st.session_state:
    st.session_state.diem_tong = 0.0

# 3. Giao diện Trang chủ
st.title("🚀 Hệ Thống Ôn Thi Tốt Nghiệp Môn Tin Học")
st.subheader("Chương trình GDPT 2018 - Hỗ trợ học sinh lớp 12")

# Tạo 2 cột để giao diện cân đối
col1, col2 = st.columns([2, 1])

with col1:
    st.info("""
    ### Chào mừng các em học sinh!
    Ứng dụng này được thiết kế để giúp các em:
    * **Luyện tập:** Theo từng chủ đề (A, B, C, D, E, F, G).
    * **Thi thử:** Cấu trúc đề chuẩn 3 phần của Bộ Giáo dục.
    * **Trợ lý AI:** Giải đáp thắc mắc về lập trình và lý thuyết Tin học.
    """)
    
    # Ô nhập tên để cá nhân hóa trải nghiệm
    ten = st.text_input("Nhập họ và tên của em để bắt đầu:", value=st.session_state.ten_hoc_sinh)
    if ten:
        st.session_state.ten_hoc_sinh = ten
        st.success(f"Chào mừng {ten}! Hãy chọn một mục ở Menu bên trái để bắt đầu ôn tập.")

with col2:
    st.image("https://img.freepik.com/free-vector/online-test-concept-illustration_114360-5536.jpg", caption="Học tập không ngừng nghỉ")

# 4. Chân trang (Footer)
st.divider()
st.markdown(
    """
    <div style='text-align: center'>
        <p>Phát triển bởi <b>Thầy Khanh</b> - Tổ trưởng chuyên môn Tin học</p>
        <p><i>Ứng dụng bám sát Công văn 7991/BGDĐT-GDTrH</i></p>
    </div>
    """, 
    unsafe_allow_status=True
)
