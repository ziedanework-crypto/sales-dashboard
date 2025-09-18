import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# تحميل البيانات
# =========================
df = pd.read_csv("dailysales.csv")

# =========================
# إعداد واجهة التطبيق
# =========================
st.set_page_config(page_title="لوحة متابعة المبيعات", page_icon="📊", layout="wide")

st.title("📊 لوحة متابعة المبيعات")
st.markdown("مرحباً بك في لوحة متابعة أداء مندوبي المبيعات")

# =========================
# KPIs (مؤشرات سريعة)
# =========================
total_sales = df["صافي المبيعات"].sum()
avg_target = df["هدف المبيعات"].mean()
achievement_rate = (df["صافي المبيعات"].sum() / df["هدف المبيعات"].sum()) * 100

col1, col2, col3 = st.columns(3)
col1.metric("إجمالي المبيعات", f"{total_sales:,.0f} جنيه")
col2.metric("متوسط الهدف", f"{avg_target:,.0f} جنيه")
col3.metric("نسبة تحقيق الأهداف", f"{achievement_rate:.2f}%")

# =========================
# عرض الجدول كامل
# =========================
st.subheader("📑 بيانات تفصيلية")
st.dataframe(df, use_container_width=True)

# =========================
# رسم بياني: المبيعات مقابل الهدف
# =========================
st.subheader("📈 مقارنة المبيعات مع الأهداف")

fig, ax = plt.subplots(figsize=(10,5))
ax.bar(df["اسم المندوب"], df["هدف المبيعات"], label="الهدف", alpha=0.6)
ax.bar(df["اسم المندوب"], df["صافي المبيعات"], label="صافي المبيعات", alpha=0.8)
ax.set_ylabel("القيمة")
ax.set_xlabel("المندوب")
ax.set_title("مقارنة المبيعات مع الهدف")
ax.legend()
st.pyplot(fig)

# =========================
# رسم بياني: نسبة تحقيق الأهداف
# =========================
st.subheader("🎯 نسبة تحقيق الهدف لكل مندوب")
st.bar_chart(df.set_index("اسم المندوب")["تحقيق الهدف"])
