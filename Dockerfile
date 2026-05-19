# 1. الصورة الأساسية لبايثون
FROM python:3.11-slim
# 2. الفولدر اللي الشغل كله هيبقى جواه جوه الكونتينر
WORKDIR /app

# 3. بنسطب الأدوات اللي بتخلي بايثون يعرف يعمل compile لمكتبة بوستجر
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# 4. نسخ ملف المكتبات وتسطيبها
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. نسخ باقي كود المشروع
COPY . .

# 6. فتح البورت اللي فلاسك شغال عليه
EXPOSE 5000

# 7. أمر تشغيل التطبيق
CMD ["python", "app.py"]