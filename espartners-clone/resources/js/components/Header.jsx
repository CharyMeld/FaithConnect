import React, { useState, useEffect } from 'react';

const Header = () => {
    const [isSticky, setIsSticky] = useState(false);
    const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

    useEffect(() => {
        const handleScroll = () => {
            setIsSticky(window.scrollY > 50);
        };
        window.addEventListener('scroll', handleScroll);
        return () => window.removeEventListener('scroll', handleScroll);
    }, []);

    return (
        <>
            {/* Top Bar */}
            <div className="top-bar">
                <div className="container">
                    <div className="top-bar-content">
                        <div className="top-bar-left">
                            <a href="mailto:info@espartners.co" className="email-link">
                                <i className="fas fa-envelope"></i> info@espartners.co
                            </a>
                        </div>
                        <div className="top-bar-right">
                            <div className="social-links">
                                <a href="https://www.facebook.com/ent4prosperity/" target="_blank" rel="noopener noreferrer">
                                    <i className="fab fa-facebook-f"></i>
                                </a>
                                <a href="https://twitter.com/es_partners" target="_blank" rel="noopener noreferrer">
                                    <i className="fab fa-twitter"></i>
                                </a>
                                <a href="https://www.instagram.com/espartners_official/" target="_blank" rel="noopener noreferrer">
                                    <i className="fab fa-instagram"></i>
                                </a>
                                <a href="https://www.linkedin.com/company/entrepreneurial-solutions-partners-llc-esp-/" target="_blank" rel="noopener noreferrer">
                                    <i className="fab fa-linkedin-in"></i>
                                </a>
                                <a href="https://www.youtube.com/@espartners1161" target="_blank" rel="noopener noreferrer">
                                    <i className="fab fa-youtube"></i>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            {/* Main Header */}
            <header className={`header ${isSticky ? 'sticky' : ''}`}>
                <div className="container">
                    <div className="header-content">
                        <div className="logo">
                            <a href="/">
                                <img src="/images/logo.png" alt="ESPartners Logo" />
                            </a>
                        </div>

                        <nav className={`main-nav ${isMobileMenuOpen ? 'active' : ''}`}>
                            <ul>
                                <li className="dropdown">
                                    <a href="/about">About</a>
                                    <ul className="dropdown-menu">
                                        <li><a href="/about">About Us</a></li>
                                        <li><a href="/our-solutions">Our Solutions</a></li>
                                        <li><a href="/our-partners">Partners/Clients</a></li>
                                        <li><a href="/career">Career</a></li>
                                    </ul>
                                </li>
                                <li className="dropdown">
                                    <a href="/our-solutions">Our Solutions</a>
                                    <ul className="dropdown-menu">
                                        <li><a href="#">Insights</a></li>
                                        <li><a href="#">Scale</a></li>
                                        <li><a href="/grow-to-scale">Grow To Scale</a></li>
                                    </ul>
                                </li>
                                <li><a href="/entrepreneurs">Entrepreneurs</a></li>
                                <li><a href="/impact-stories">Impact stories</a></li>
                                <li><a href="/blog">Blog</a></li>
                            </ul>
                        </nav>

                        <div className="header-right">
                            <a href="/contact-us" className="contact-btn">
                                <img src="/images/contact-icon.png" alt="Contact" />
                                <span>Contact Us</span>
                            </a>
                        </div>

                        <button
                            className="mobile-menu-toggle"
                            onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
                        >
                            <span></span>
                            <span></span>
                            <span></span>
                        </button>
                    </div>
                </div>
            </header>
        </>
    );
};

export default Header;
