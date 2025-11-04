import React from 'react';
import CountUp from 'react-countup';
import { useInView } from 'react-intersection-observer';

const Statistics = () => {
    const { ref, inView } = useInView({
        triggerOnce: true,
        threshold: 0.3,
    });

    const stats = [
        { id: 1, value: 22, suffix: '+', title: 'Countries covered' },
        { id: 2, value: 29, suffix: '+', title: 'Projects implemented around Africa' },
        { id: 3, value: 303, suffix: '', title: 'SMEs accelerated' },
        { id: 4, value: 276, suffix: '', title: 'SMEs incubated' },
        { id: 5, value: 7821, suffix: '', title: 'Young men and women reached with inspiration messages on entrepreneurial mindset' },
        { id: 6, value: 1051, suffix: '', title: 'Jobs created' },
    ];

    return (
        <section className="statistics-section" ref={ref}>
            <div className="container">
                <div className="section-header text-center">
                    <h2 className="section-title">Our reach and impact in 2023</h2>
                </div>

                <div className="statistics-grid">
                    {stats.map((stat) => (
                        <div key={stat.id} className="stat-item">
                            <div className="stat-number">
                                {inView && (
                                    <CountUp
                                        end={stat.value}
                                        duration={2.5}
                                        separator=","
                                        suffix={stat.suffix}
                                    />
                                )}
                            </div>
                            <div className="stat-title">{stat.title}</div>
                        </div>
                    ))}
                </div>
            </div>
        </section>
    );
};

export default Statistics;
