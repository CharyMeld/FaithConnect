import React from 'react';

const DataSection = () => {
    return (
        <section className="data-section">
            <div className="container">
                <div className="data-grid">
                    <div className="data-content-col">
                        <span className="section-subtitle">Driven by data</span>
                        <h2 className="section-title">
                            We believe in the power of entrepreneurs to foster prosperity in Africa
                        </h2>

                        <div className="data-features">
                            <div className="data-feature-item">
                                <div className="data-feature-icon">
                                    <img src="/images/icon-job-creation.png" alt="Job Creation" />
                                </div>
                                <div className="data-feature-content">
                                    <h3>Job Creation</h3>
                                    <p>As our entrepreneurs continue to forge sustainable businesses, they in turn create opportunities of employment for people.</p>
                                </div>
                            </div>

                            <div className="data-feature-item">
                                <div className="data-feature-icon">
                                    <img src="/images/icon-women-inclusion.png" alt="Women Inclusion" />
                                </div>
                                <div className="data-feature-content">
                                    <h3>Women Inclusion</h3>
                                    <p>With deliberate strategies that encourage and support the participation of women in our entrepreneurship programs, we continue to strive for inclusion.</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div className="data-chart-col">
                        <div className="chart-wrapper">
                            <canvas id="growthChart"></canvas>
                        </div>
                        <p className="chart-caption">
                            We are working with entrepreneurs to create sustainable impact for Africa
                        </p>
                    </div>
                </div>
            </div>
        </section>
    );
};

export default DataSection;
