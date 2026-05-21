# Vercel Note
# Vercel does NOT support permanent local file uploads.
# So this version stores uploaded HTML files inside browser localStorage.
# Best for personal article hosting.

from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>HTML Article CMS</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, sans-serif;
        }

        body {
            display: flex;
            height: 100vh;
            overflow: hidden;
            background: #f3f4f6;
        }

        .sidebar {
            width: 300px;
            background: #111827;
            color: white;
            overflow-y: auto;
            padding: 20px;
        }

        .sidebar h2 {
            margin-bottom: 20px;
        }

        .article-item {
            padding: 12px;
            border-radius: 8px;
            background: #1f2937;
            margin-bottom: 10px;
            cursor: pointer;
            transition: 0.2s;
            word-break: break-word;
        }

        .article-item:hover {
            background: #374151;
        }

        .main {
            flex: 1;
            display: flex;
            flex-direction: column;
        }

        .topbar {
            padding: 15px;
            background: white;
            border-bottom: 1px solid #ddd;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .content {
            flex: 1;
            overflow: auto;
            background: white;
        }

        iframe {
            width: 100%;
            height: 100%;
            border: none;
        }

        button {
            background: #2563eb;
            color: white;
            border: none;
            padding: 10px 18px;
            border-radius: 8px;
            cursor: pointer;
        }

        button:hover {
            background: #1d4ed8;
        }

        input[type=file] {
            display: none;
        }

        .empty {
            padding: 50px;
            font-size: 22px;
            color: #666;
        }
    </style>
</head>
<body>

<div class="sidebar">
    <h2>Articles</h2>
    <div id="articles"></div>
</div>

<div class="main">
    <div class="topbar">
        <h3>HTML Article CMS</h3>

        <div>
            <label for="file-upload">
                <button>Upload HTML</button>
            </label>
            <input type="file" id="file-upload" accept=".html">
        </div>
    </div>

    <div class="content" id="content">
        <div class="empty">
            Upload HTML files to view them here.
        </div>
    </div>
</div>

<script>
    let articles = JSON.parse(localStorage.getItem('articles') || '[]');

    function saveArticles() {
        localStorage.setItem('articles', JSON.stringify(articles));
    }

    function renderSidebar() {
        const container = document.getElementById('articles');
        container.innerHTML = '';

        articles.forEach((article, index) => {
            const div = document.createElement('div');
            div.className = 'article-item';
            div.innerText = article.name;

            div.onclick = () => openArticle(index);

            container.appendChild(div);
        });
    }

    function openArticle(index) {
        const article = articles[index];

        document.getElementById('content').innerHTML = `
            <iframe srcdoc="${article.content.replace(/"/g, '&quot;')}"></iframe>
        `;
    }

    document.getElementById('file-upload').addEventListener('change', async (e) => {
        const file = e.target.files[0];

        if (!file) return;

        const text = await file.text();

        articles.push({
            name: file.name,
            content: text
        });

        saveArticles();
        renderSidebar();
        openArticle(articles.length - 1);
    });

    renderSidebar();

    if (articles.length > 0) {
        openArticle(0);
    }
</script>

</body>
</html>
"""


@app.route("/")
def home():
    return HTML


if __name__ == "__main__":
    app.run(debug=True)

"""

VERCEL DEPLOYMENT

1. Create files:

project/
│
├── app.py
├── requirements.txt
└── vercel.json

2. requirements.txt

flask

3. vercel.json

{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}

4. Deploy:

vercel

FEATURES

- Upload HTML pages
- Sidebar article list
- Instant preview
- Modern UI
- Vercel compatible
- No database needed
- Stores articles in browser localStorage

IMPORTANT

Because Vercel server storage is temporary, uploaded files are stored in browser localStorage.

If you want:

- permanent cloud storage
- login system
- markdown editor
- categories/tags
- SEO pages
- admin dashboard
- drag-drop upload

then next step should be:

Frontend: Next.js
Storage: Supabase / Firebase / S3

"""
