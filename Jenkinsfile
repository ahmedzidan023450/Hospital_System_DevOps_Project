pipeline {
    // بنقول لجينكنز يشتغل على أي Agent متاح عندك
    agent any 

    stages {
        // المرحلة الأولى: سحب الكود من جيت هاب
        stage('Fetch Code') {
            steps {
                echo 'جاري سحب أحدث كود من GitHub...'
                checkout scm
            }
        }

        // المرحلة الثانية: التأكد إن الكود سليم ومفهوش أخطاء كتابية
        stage('Sanity Check') {
            steps {
                echo 'جاري فحص ملفات البايثون...'
                // الأمر ده بيتأكد إن ملف app.py ملوش أخطاء Syntax
                sh 'python -m py_compile app.py' 
            }
        }

        // المرحلة الثالثة: الـ Deployment الحقيقي باستخدام دوكر كومبوز
        stage('Deploy to Docker') {
            steps {
                echo 'جاري تحديث الكونتينرز وتشغيل المستشفى...'
                // الأوامر اللي إنت كنت بتكتبها بايدك، جينكنز هيشغلها في الـ Terminal لوحده
                sh 'docker-compose down'
                sh 'docker-compose up -d --build'
            }
        }
    }
}