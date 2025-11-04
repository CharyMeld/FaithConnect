import React from 'react';

const Blog = () => {
    const blogPosts = [
        {
            id: 1,
            title: "FSE 2025 : La finance verte, levier stratégique pour les PME ivoiriennes",
            date: "20 May",
            author: "update",
            category: "Business",
            image: "/images/blog-1.jpg",
            link: "#"
        },
        {
            id: 2,
            title: "A Journey of Insight, Innovation, and Impact in Eastern Rwanda",
            date: "14 May",
            author: "update",
            category: "Business",
            image: "/images/blog-2.jpg",
            link: "#"
        },
        {
            id: 3,
            title: "8 mars 2025 : Regards croisés de nos Super Women sur l'autonomisation",
            date: "07 Mar",
            author: "Jean Luc",
            category: "Uncategorized",
            image: "/images/blog-3.jpg",
            link: "#"
        }
    ];

    return (
        <section className="blog-section">
            <div className="container">
                <div className="section-header text-center">
                    <span className="section-subtitle">Leadership Thoughts</span>
                    <h2 className="section-title">Latest information & business updates from us</h2>
                </div>

                <div className="blog-grid">
                    {blogPosts.map((post) => (
                        <div key={post.id} className="blog-card">
                            <div className="blog-image">
                                <img src={post.image} alt={post.title} />
                                <div className="blog-date">
                                    <span className="date-text">{post.date}</span>
                                </div>
                            </div>
                            <div className="blog-content">
                                <div className="blog-meta">
                                    <span className="meta-author">
                                        <i className="fas fa-user"></i> {post.author}
                                    </span>
                                    <span className="meta-category">
                                        <i className="fas fa-folder"></i> {post.category}
                                    </span>
                                </div>
                                <h3 className="blog-title">
                                    <a href={post.link}>{post.title}</a>
                                </h3>
                                <a href={post.link} className="blog-link">
                                    Know More <i className="fas fa-arrow-right"></i>
                                </a>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </section>
    );
};

export default Blog;
