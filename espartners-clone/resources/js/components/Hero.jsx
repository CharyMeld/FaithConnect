import React, { useState, useEffect } from 'react';

const Hero = () => {
    const [currentSlide, setCurrentSlide] = useState(0);

    const slides = [
        {
            id: 1,
            title: "Leveraging intelligent capital to nurture the African prosperity ecosystem",
            image: "/images/hero-slide-1.jpg"
        },
        {
            id: 2,
            title: "More than 22 years of experience in private sector development and insight strategy advisory",
            image: "/images/hero-slide-2.jpg"
        }
    ];

    useEffect(() => {
        const timer = setInterval(() => {
            setCurrentSlide((prev) => (prev + 1) % slides.length);
        }, 5000);
        return () => clearInterval(timer);
    }, []);

    return (
        <section className="hero-section">
            <div className="hero-slider">
                {slides.map((slide, index) => (
                    <div
                        key={slide.id}
                        className={`hero-slide ${index === currentSlide ? 'active' : ''}`}
                        style={{ backgroundImage: `url(${slide.image})` }}
                    >
                        <div className="hero-overlay"></div>
                        <div className="container">
                            <div className="hero-content">
                                <h1 className="hero-title">{slide.title}</h1>
                            </div>
                        </div>
                    </div>
                ))}
            </div>

            <div className="hero-nav">
                {slides.map((_, index) => (
                    <button
                        key={index}
                        className={`hero-nav-btn ${index === currentSlide ? 'active' : ''}`}
                        onClick={() => setCurrentSlide(index)}
                    >
                        <span>{index + 1}</span>
                    </button>
                ))}
            </div>
        </section>
    );
};

export default Hero;
