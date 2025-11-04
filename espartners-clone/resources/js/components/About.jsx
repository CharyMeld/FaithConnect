import React from 'react';

const About = () => {
    return (
        <section className="about-section">
            <div className="container">
                <div className="about-grid">
                    <div className="about-image-col">
                        <div className="about-image-wrapper">
                            <img src="/images/eric-kacou.jpg" alt="Eric Kacou" />
                            <div className="quote-icon">
                                <i className="fas fa-quote-left"></i>
                            </div>
                            <div className="quote-content">
                                <h3 className="quote-text">
                                    "Enough evidence that points to Africa as a fertile environment for entrepreneurship has been given. ESP is happy to be of impact to the action takers"
                                </h3>
                                <p className="quote-author">Eric Kacou - Co founder</p>
                            </div>
                        </div>
                    </div>

                    <div className="about-content-col">
                        <div className="about-header">
                            <span className="section-subtitle">About us</span>
                            <h2 className="section-title">Experts in Private sector development</h2>
                            <p className="section-description">
                                "Entrepreneurs investing in Entrepreneurs." We believe that sustainable transformation requires an entrepreneurial approach to deploy scalable and innovative solutions to foster prosperity.
                            </p>
                        </div>

                        <div className="about-features">
                            <div className="feature-item">
                                <div className="feature-icon">
                                    <img src="/images/icon-technical.svg" alt="Technical Assistance" />
                                </div>
                                <div className="feature-content">
                                    <h3 className="feature-title">Technical assistance</h3>
                                    <p className="feature-text">
                                        Through our rigorous and thoroughly designed processes, we select and nurture potential high-impact SMEs through our flagship programs.
                                    </p>
                                </div>
                            </div>

                            <div className="feature-item">
                                <div className="feature-icon">
                                    <img src="/images/icon-financial.svg" alt="Financial Support" />
                                </div>
                                <div className="feature-content">
                                    <h3 className="feature-title">Financial support</h3>
                                    <p className="feature-text">
                                        We support our entrepreneurs with strategic funding to promote the emergence of Pan-African champions.
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    );
};

export default About;
