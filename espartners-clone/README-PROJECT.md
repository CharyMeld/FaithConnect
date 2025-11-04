# ESPartners Website Clone - Laravel + React

A modern clone of the espartners.co website built with Laravel backend and React frontend using Vite.

## 🚀 Features

### Frontend (React)
- **Modern React Components**: Fully functional component-based architecture
- **Responsive Design**: Mobile-first approach with responsive breakpoints
- **Smooth Animations**: Fade-in effects and hover transitions
- **Interactive Elements**:
  - Sticky navigation header
  - Auto-playing hero slider
  - Animated counters with intersection observer
  - Dropdown menus
  - Mobile hamburger menu

### Components Built
1. **Header** - Sticky navigation with dropdown menus
2. **Hero** - Auto-sliding hero section with 2 slides
3. **CoreValues** - 4 value cards (Passion, Agility, Collaboration, Equity)
4. **Solutions** - Two-column layout showcasing Insights and Scale
5. **About** - Grid layout with quote and feature highlights
6. **Statistics** - Animated counters showing company metrics
7. **DataSection** - Data visualization section
8. **Blog** - Three-column blog card grid
9. **Footer** - Multi-column footer with newsletter signup

### Design System
- **Primary Color**: `#f05a2b` (Orange)
- **Secondary Color**: `#142355` (Dark Blue)
- **Fonts**:
  - Rubik (Primary)
  - Merriweather (Headings)
  - Poppins (Secondary)

## 📦 Tech Stack

- **Backend**: Laravel 12.x
- **Frontend**: React 18
- **Build Tool**: Vite
- **Styling**: Custom CSS (No framework)
- **Router**: React Router DOM
- **Animations**: React CountUp, React Intersection Observer
- **Slider**: Swiper (optional)

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd espartners-clone
```

2. **Install PHP dependencies**
```bash
composer install
```

3. **Install Node dependencies**
```bash
npm install
```

4. **Environment Setup**
```bash
cp .env.example .env
php artisan key:generate
```

5. **Database Setup**
```bash
php artisan migrate
```

6. **Run Development Servers**

Terminal 1 (Laravel):
```bash
php artisan serve
```

Terminal 2 (Vite):
```bash
npm run dev
```

Visit: `http://localhost:8000`

## 📁 Project Structure

```
espartners-clone/
├── app/
├── bootstrap/
├── config/
├── database/
├── public/
├── resources/
│   ├── css/
│   │   └── app.css          # Main CSS file
│   ├── js/
│   │   ├── components/      # React components
│   │   │   ├── Header.jsx
│   │   │   ├── Hero.jsx
│   │   │   ├── CoreValues.jsx
│   │   │   ├── Solutions.jsx
│   │   │   ├── About.jsx
│   │   │   ├── Statistics.jsx
│   │   │   ├── DataSection.jsx
│   │   │   ├── Blog.jsx
│   │   │   └── Footer.jsx
│   │   ├── App.jsx          # Main App component
│   │   └── app.jsx          # React entry point
│   └── views/
│       └── app.blade.php    # Main Laravel view
├── routes/
│   └── web.php              # Routes configuration
├── vite.config.js           # Vite configuration
└── package.json             # NPM dependencies
```

## 🎨 Component Details

### Header Component
- Top bar with email and social media links
- Main navigation with dropdown menus
- Sticky header on scroll
- Mobile responsive hamburger menu
- Contact Us button

### Hero Component
- Auto-playing slider with 2 slides
- Overlay effect on images
- Animated text
- Navigation dots

### CoreValues Component
- 4-column grid layout
- SVG icons
- Hover effects with scale transformation

### Solutions Component
- Featured "Insights" and "Scale" sections
- Image cards with overlay dates
- Descriptive content
- Call-to-action buttons

### About Component
- Two-column grid
- Quote section with founder's message
- Feature highlights (Technical Assistance, Financial Support)
- Icon-based layout

### Statistics Component
- Animated counters using CountUp
- Intersection Observer for triggering animations
- 6 key metrics displayed
- Responsive grid layout

### Blog Component
- 3-column blog card layout
- Featured images
- Meta information (author, category, date)
- Hover effects

### Footer Component
- Newsletter signup form
- Contact information (Rwanda & Côte d'Ivoire offices)
- Useful links
- Social media links
- Copyright information

## 🌐 API Endpoints (To be implemented)

```php
// routes/api.php
Route::get('/solutions', [SolutionController::class, 'index']);
Route::get('/blog-posts', [BlogController::class, 'index']);
Route::get('/statistics', [StatisticsController::class, 'index']);
Route::post('/newsletter', [NewsletterController::class, 'subscribe']);
```

## 🎯 Next Steps

1. **Add Images**: Place actual images in `public/images/` directory
   - Logo (logo.png)
   - Hero slides (hero-slide-1.jpg, hero-slide-2.jpg)
   - Solution images (insights.jpg, scale.jpg)
   - About image (eric-kacou.jpg)
   - Blog images (blog-1.jpg, blog-2.jpg, blog-3.jpg)
   - Icons (SVG files)

2. **Backend API**: Create Laravel controllers and models for:
   - Solutions
   - Blog posts
   - Statistics
   - Newsletter subscriptions

3. **Database**: Create migrations and seeders

4. **Connect Frontend to API**: Update React components to fetch data from Laravel API

5. **Additional Features**:
   - Contact form functionality
   - Search functionality
   - Blog pagination
   - Admin panel for content management

## 📱 Responsive Breakpoints

- Desktop: 1024px+
- Tablet: 768px - 1023px
- Mobile: < 768px

## 🔧 Configuration

### Vite Config
```javascript
// vite.config.js
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import laravel from 'laravel-vite-plugin';

export default defineConfig({
    plugins: [
        laravel({
            input: ['resources/css/app.css', 'resources/js/app.jsx'],
            refresh: true,
        }),
        react(),
    ],
    resolve: {
        alias: {
            '@': '/resources/js',
        },
    },
});
```

## 📄 License

This is a clone project for educational purposes.

## 👥 Credits

- Original Website: [espartners.co](https://espartners.co)
- Framework: Laravel & React
- Build Tool: Vite

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

For issues and questions, please open an issue in the repository.

---

Built with ❤️ using Laravel and React
