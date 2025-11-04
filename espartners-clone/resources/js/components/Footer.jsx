import React from 'react';

const Footer = () => {
    return (
        <footer className="footer">
            {/* Newsletter Section */}
            <div className="footer-newsletter">
                <div className="container">
                    <div className="newsletter-grid">
                        <div className="newsletter-image">
                            <img src="/images/entrepreneurs.png" alt="Meet our entrepreneurs" />
                        </div>
                        <div className="newsletter-content">
                            <h3 className="newsletter-title">Meet our awesome entrepreneurs</h3>
                            <a href="/entrepreneurs" className="btn btn-primary">View More</a>
                        </div>
                    </div>
                </div>
            </div>

            {/* Footer Main */}
            <div className="footer-main">
                <div className="container">
                    <div className="footer-grid">
                        <div className="footer-col">
                            <h4 className="footer-title">Contact us</h4>
                            <ul className="footer-contact">
                                <li>
                                    <i className="fas fa-map-marker-alt"></i>
                                    <span>Rwanda: KG 05 Street, Kacyiru, Gasabo, Kigali. Fair View Building</span>
                                </li>
                                <li>
                                    <i className="fas fa-map-marker-alt"></i>
                                    <span>Cocody, II Plateaux, Rue Saint Jacques 28 BP131, Côte d'Ivoire</span>
                                </li>
                                <li>
                                    <i className="fas fa-phone-alt"></i>
                                    <span>Phone: +225 22 41 42 49</span>
                                </li>
                                <li>
                                    <i className="fas fa-envelope"></i>
                                    <span>Email: info@espartners.co</span>
                                </li>
                            </ul>
                        </div>

                        <div className="footer-col">
                            <h4 className="footer-title">Useful Links</h4>
                            <ul className="footer-links">
                                <li><a href="/about">About us</a></li>
                                <li><a href="/team">Our People</a></li>
                                <li><a href="/our-solutions">ESP Scale</a></li>
                                <li><a href="/blog">Blog</a></li>
                            </ul>
                        </div>

                        <div className="footer-col">
                            <h4 className="footer-title">&nbsp;</h4>
                            <ul className="footer-links">
                                <li><a href="#">ESP Insights</a></li>
                                <li><a href="/our-partners">Our Partners</a></li>
                                <li><a href="/impact-stories">Impact Stories</a></li>
                                <li><a href="/career">Careers</a></li>
                            </ul>
                        </div>

                        <div className="footer-col">
                            <h4 className="footer-title">Subscribe to our newsletter</h4>
                            <p>Sign up for our latest news & articles. We won't give you spam mails.</p>
                            <form className="newsletter-form">
                                <input
                                    type="email"
                                    placeholder="Enter your email..."
                                    className="form-input"
                                    required
                                />
                                <button type="submit" className="form-submit">
                                    <i className="far fa-paper-plane"></i>
                                </button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>

            {/* Footer Bottom */}
            <div className="footer-bottom">
                <div className="container">
                    <div className="footer-bottom-content">
                        <p className="copyright">
                            Copyright © 2023 Entrepreneurial Solutions Partners
                        </p>
                        <div className="footer-social">
                            <a href="https://www.facebook.com/ent4prosperity/">facebook</a>
                            <a href="https://twitter.com/es_partners">twitter</a>
                            <a href="https://instagram.com/espartners_official">instragram</a>
                            <a href="https://www.linkedin.com/company/entrepreneurial-solutions-partners-llc-esp-">Linkedin</a>
                        </div>
                    </div>
                </div>
            </div>
        </footer>
    );
};

export default Footer;
