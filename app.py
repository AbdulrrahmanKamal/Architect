from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# بيانات المشاريع
projects = [
    {
        'id': 1,
        'title': 'فيلا عصرية',
        'architect': 'Abdulrahman Kamal',
        'location': 'Erbil، Iraq',
        'area': '750 م²',
        'year': '2025',
        'description': 'تصميم فيلا عصرية  ',
        'image': 'villa.jpg',
        'image_url': 'https://cdnassets.hw.net/dims4/GG/f6a91a8/2147483647/resize/850x%3E/quality/90/?url=https%3A%2F%2Fcdnassets.hw.net%2Fab%2Fc1%2Ffc52560248ab8f3d50a8cee6233d%2F42a804f679924d2191e92c7085e10595.jpg',
        'has_details': True
    },
    {
        'id': 2,
        'title': 'برج سكني',
        'architect': 'Abdulrahman Kamal',
        'location': 'Kirkuk, Iraq',
        'area': '12000 م²',
        'year': '2025',
        'description': 'برج سكني  ',
        'image': 'tower.jpg',
        'image_url': 'https://s3-eu-west-1.amazonaws.com/content.argaamnews.com/838cb051-2516-447f-9de2-103a0ca91713.jpg',
        'has_details': False
    }
]

# بيانات الخدمات
services = [
    {'title': 'التصميم المعماري', 'icon': 'fa-building'},
    {'title': 'التخطيط ', 'icon': 'fa-city'},
    {'title': 'التصميم الداخلي', 'icon': 'fa-couch'},
    {'title': 'الاستشارات', 'icon': 'fa-comments'}
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects[:3], services=services)

@app.route('/projects')
def all_projects():
    return render_template('projects.html', projects=projects)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = next((p for p in projects if p['id'] == project_id), None)
    if project:
        if project['title'] == 'فيلا عصرية':
            project['additional_images'] = [
                "https://cdnassets.hw.net/dims4/GG/ea28f0b/2147483647/resize/850x%3E/quality/90/?url=https%3A%2F%2Fcdnassets.hw.net%2Fa8%2F64%2F814bb84c4d93aa9019d3cdb11d2d%2F373f5b7d45534526927f2ebcf39ab20d.jpg",
                "https://cdnassets.hw.net/dims4/GG/52d3e65/2147483647/resize/850x%3E/quality/90/?url=https%3A%2F%2Fcdnassets.hw.net%2F08%2F2e%2F3bd2c7834da4a5850d14de187081%2F97ea3dad98834e01a61ca7731dee257e.jpg",
                "https://cdnassets.hw.net/dims4/GG/3a38849/2147483647/resize/850x%3E/quality/90/?url=https%3A%2F%2Fcdnassets.hw.net%2F0a%2F64%2Ffef6a374470699f4e120b30821cb%2F5db27773d06b42a884fe33b912adf203.jpg"
            ]
            project['description_details'] = """
                <h3 class="section-title">التصميم الخارجي</h3>
                <p>تتميز الفيلا بمزيج متناغم من الحجر والزجاج والمعادن. تُبرز الألوان المحايدة الجمال الطبيعي للمواد، بينما تسمح النوافذ الواسعة بدخول ضوء طبيعي وافر إلى الداخل. تُضفي الأنماط الهندسية على الواجهة مظهرًا مميزًا، مما يُضفي عليها لمسة عصرية خالدة.</p>

                <h3 class="section-title">العناصر المعمارية</h3>
                <p>يُركّز التصميم المعماري على الخطوط النظيفة والتصميم البسيط. تُضفي العناصر الرأسية والأفقية مظهرًا متوازنًا ومتماسكًا. تُضفي اللمسات المعدنية والشرائح الخشبية عمقًا وملمسًا مميزًا على التصميم الخارجي، بينما تُبرز الإضاءة المُوزّعة بشكل استراتيجي السمات المعمارية.</p>

                <h3 class="section-title">تصميم الإضاءة</h3>
                <p>تلعب الإضاءة دورًا محوريًا في تعزيز جاذبية الفيلا. تُبرز الإضاءة الخارجية العناصر المعمارية، مما يخلق تأثيرًا خلابًا في الليل. تُسهم مصابيح LED على طول الممرات وحول محيط الفيلا في إضفاء أجواء مميزة، مما يجعل الفيلا مميزة.</p>

                <h3 class="section-title">تكامل المناظر الطبيعية</h3>
                <p>تندمج الفيلا بسلاسة مع المناظر الطبيعية المحيطة بها. الحجر الطبيعي والمساحات الخضراء تخلق بيئة هادئة. توفر مناطق الجلوس الخارجية مساحة للاسترخاء والترفيه، بينما تضفي الحدائق المُعتنى بها بعناية سحرًا خاصًا.</p>

                <h3 class="section-title">المساحات الداخلية</h3>
                <p>يُولي التصميم الداخلي الأولوية للمساحات المفتوحة والانتقالات السلسة بين الغرف. تضمن النوافذ الكبيرة وفرة الضوء الطبيعي في جميع أنحاء المنزل. يُضفي أسلوب الديكور البسيط مظهرًا أنيقًا ومرتبًا، مع التركيز على الراحة والأناقة.</p>
            """
        return render_template('project_detail.html', project=project)
    return redirect(url_for('home'))

@app.route('/services')
def our_services():
    return render_template('services.html', services=services)

if __name__ == '__main__':
    app.run(debug=True)