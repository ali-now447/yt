FROM python:3.10-slim

# تعيين مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ ملفات المشروع إلى مجلد العمل في الحاوية
COPY . /app

# تثبيت المتطلبات إذا كان هناك ملف requirements.txt
RUN pip install --no-cache-dir -r requirements.txt || true

# فتح منفذ 8085 (اختياري، حسب حاجتك)
EXPOSE 8085

# تعيين الأمر الافتراضي لتشغيل سكربت بايثون
CMD bash start