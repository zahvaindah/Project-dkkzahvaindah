import streamlit as st

st.title("Tugas Dkk ")
st.markdown(
    """ 
    Zahva Indah N.(35) X TJKT 1 
    """
)
def calculate(num1, num2, operation):
    """Melakukan perhitungan berdasarkan operasi yang dipilih."""
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        # Pencegahan pembagian dengan nol
        return num1 / num2 if num2 != 0 else "Error: Dibagi nol"
    return None

# --- Tampilan Aplikasi ---
st.title("➕➖ Kalkulator  Sederhana")

col1, col2, col3 = st.columns(3)

with col1:
    # Input Angka Pertama
    num1 = st.number_input("Angka Pertama", value=0.0, step=1.0)

with col2:
    # Dropdown untuk memilih operasi
    operation = st.selectbox(
        "Pilih Operasi",
        ('+', '-', '*', '/')
    )

with col3:
    # Input Angka Kedua
    num2 = st.number_input("Angka Kedua", value=0.0, step=1.0)
    
st.markdown("---") # Garis pemisah

# --- Perhitungan & Tampilan Hasil ---
if st.button("Hitung"):
    result = calculate(num1, num2, operation)
    
    st.subheader("Hasil:")
    
    if isinstance(result, str) and "Error" in result:
        st.error(result)
    else:
        # Menampilkan hasil dalam format yang mudah dibaca
        st.success(f"**{num1} {operation} {num2} = {result}**")

if st.button("Send balloons!"):
    st.balloons()
    
