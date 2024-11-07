# ใช้ Python base image
FROM python:3.12-slim

# ตั้งค่า directory ทำงานใน container
WORKDIR /app

# คัดลอกไฟล์ requirements.txt และติดตั้ง dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอกไฟล์ทั้งหมดจากโฟลเดอร์โปรเจกต์ไปยัง container
COPY . .

# เปิดพอร์ต 5000 สำหรับการเชื่อมต่อแอป Flask
EXPOSE 5000

# รันแอป Flask
CMD ["python", "app.py"]
