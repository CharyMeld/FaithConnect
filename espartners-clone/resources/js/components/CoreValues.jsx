import React from 'react';

const CoreValues = () => {
    const values = [
        {
            id: 1,
            title: "Passion",
            icon: (
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 511.03 511.03">
                    <path d="M256.5,0c6.3,1.18,10.47,4.73,11.8,11.09,1,4.63-1.1,8.33-4.36,11.44-4,3.81-8.81,4.6-13.68,2.31-4.34-2-8.25-8.1-7.95-12.32.34-4.73,4.47-10.21,8.85-11.67,1.09-.36,2.23-.57,3.34-.85Z"/>
                </svg>
            )
        },
        {
            id: 2,
            title: "Agility",
            icon: (
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 463.57 469.46">
                    <path d="M168.45,384.24c-.62-11.45,1.47-24.61-3-37.45-4.6-13.27-11.26-25.47-18.08-37.63"/>
                </svg>
            )
        },
        {
            id: 3,
            title: "Collaboration",
            icon: (
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 496.76 429.33">
                    <path d="M320.37,197.47c0,18.22-.11,36.44,0,54.66.11,13.91-5.19,24.15-19,28.52"/>
                </svg>
            )
        },
        {
            id: 4,
            title: "Equity",
            icon: (
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 486.96 418.79">
                    <path d="M286.25,418.79c-3.4-6.06-2.05-12.68-2-19.06"/>
                </svg>
            )
        }
    ];

    return (
        <section className="core-values-section">
            <div className="container">
                <div className="core-values-grid">
                    {values.map((value, index) => (
                        <div
                            key={value.id}
                            className="core-value-item"
                            style={{ animationDelay: `${index * 0.1}s` }}
                        >
                            <div className="value-icon">
                                {value.icon}
                            </div>
                            <h3 className="value-title">{value.title}</h3>
                        </div>
                    ))}
                </div>
            </div>
        </section>
    );
};

export default CoreValues;
