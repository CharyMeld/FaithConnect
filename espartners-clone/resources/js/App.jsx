import React from 'react';
import Header from './components/Header';
import Hero from './components/Hero';
import CoreValues from './components/CoreValues';
import Solutions from './components/Solutions';
import About from './components/About';
import Statistics from './components/Statistics';
import DataSection from './components/DataSection';
import Blog from './components/Blog';
import Footer from './components/Footer';

function App() {
    return (
        <div className="App">
            <Header />
            <Hero />
            <CoreValues />
            <Solutions />
            <About />
            <Statistics />
            <DataSection />
            <Blog />
            <Footer />
        </div>
    );
}

export default App;
