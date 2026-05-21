import { useState, useEffect } from 'react';
import { BrowserRouter, Routes, Route, Link, useParams } from 'react-router-dom';
import articles from './articles-index.json';

// 1. Component to fetch and display the selected HTML file
function ArticleViewer() {
  const { filename } = useParams();
  const [htmlContent, setHtmlContent] = useState('Loading article...');

  useEffect(() => {
    // Fetches the HTML file directly out of the public/articles folder
    fetch(`/articles/${filename}.html`)
      .then((res) => {
        if (!res.ok) throw new Error('File not found');
        return res.text();
      })
      .then((data) => setHtmlContent(data))
      .catch(() => setHtmlContent('<h2>⚠️ Article Not Found</h2><p>The requested file could not be loaded.</p>'));
  }, [filename]);

  return (
    <div>
      <div style={{ marginBottom: '20px', color: '#71717a', fontSize: '0.85rem' }}>
        Viewing file: <code style={{ background: '#f4f4f5', padding: '2px 6px', borderRadius: '4px' }}>{filename}.html</code>
      </div>
      {/* Inject raw HTML into the wrapper */}
      <article dangerouslySetInnerHTML={{ __html: htmlContent }} />
    </div>
  );
}

// 2. Simple fallback landing page
function Home() {
  return (
    <div style={{ textAlign: 'center', marginTop: '100px', color: '#71717a' }}>
      <h1>HTML Document Hub</h1>
      <p>Pick a document from the left sidebar to start reading.</p>
    </div>
  );
}

// 3. Complete structural Layout
export default function App() {
  return (
    <BrowserRouter>
      <div style={{ display: 'flex', minHeight: '100vh', fontFamily: 'system-ui, sans-serif' }}>

        {/* Sidebar */}
        <aside style={{ width: '260px', background: '#f4f4f5', padding: '20px', borderRight: '1px solid #e4e4e7' }}>
          <h2 style={{ fontSize: '1.1rem', marginBottom: '20px', color: '#18181b' }}>📁 My HTML Uploads</h2>
          <nav style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            <Link href="/" to="/" style={{ textDecoration: 'none', color: '#09090b', fontWeight: '600' }}>🏠 Dashboard</Link>
            <hr style={{ border: 'none', borderTop: '1px solid #e4e4e7', margin: '10px 0' }} />

            {articles.length === 0 ? (
              <span style={{ fontSize: '0.9rem', color: '#a1a1aa', fontStyle: 'italic' }}>No .html files found</span>
            ) : (
              articles.map((slug) => (
                <Link
                  key={slug}
                  to={`/article/${slug}`}
                  style={{ textDecoration: 'none', color: '#27272a', fontSize: '0.95rem', textTransform: 'capitalize' }}
                >
                  📄 {slug.replace(/-/g, ' ')}
                </Link>
              ))
            )}
          </nav>
        </aside>

        {/* Content Area */}
        <main style={{ flex: 1, padding: '40px', background: '#ffffff' }}>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/article/:filename" element={<ArticleViewer />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}