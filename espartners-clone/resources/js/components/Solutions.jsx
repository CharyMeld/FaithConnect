import React from 'react';

const Solutions = () => {
    return (
        <section className="solutions-section">
            <div className="container">
                <div className="solutions-header">
                    <div className="section-title-wrapper">
                        <h2 className="section-title">Explore Solutions</h2>
                    </div>
                    <div className="section-description">
                        <p>Our services can be categorized into two - Insights and Scale. Collectively, ESP provides a complete ecosystem of support for institutions of any size and ventures at any stage - all with varying strategic needs.</p>
                    </div>
                    <div className="section-button">
                        <a href="/our-solutions" className="btn btn-primary">LEARN MORE</a>
                    </div>
                </div>

                <div className="solutions-grid">
                    <div className="solution-card">
                        <div className="solution-image">
                            <img src="/images/insights.jpg" alt="Insights" />
                            <div className="solution-date">
                                <span className="date-number">01</span>
                            </div>
                        </div>
                        <div className="solution-content">
                            <h3 className="solution-title">Insights</h3>
                            <p className="solution-text">
                                This practice focuses on working directly with entrepreneurs at all stages of growth. From pre-ideation, to ideation, to startup and beyond; we design and implement entrepreneurial support programs to help entrepreneurs across Africa scale their businesses, to foster their businesses into commercially successful, disruptive businesses.
                            </p>
                        </div>
                    </div>

                    <div className="solution-card">
                        <div className="solution-image">
                            <img src="/images/scale.jpg" alt="Scale" />
                            <div className="solution-date">
                                <span className="date-number">02</span>
                            </div>
                        </div>
                        <div className="solution-content">
                            <h3 className="solution-title">Scale</h3>
                            <p className="solution-text">
                                This practice focuses on working directly with entrepreneurs at all stages of growth. From pre-ideation, to ideation, to startup and beyond; we design and implement entrepreneurial support programs to help entrepreneurs across Africa scale their businesses, to foster their businesses into commercially successful, disruptive businesses.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    );
};

export default Solutions;
