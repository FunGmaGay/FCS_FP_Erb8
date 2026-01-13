// JS for Carousel

        const carousel = document.querySelector('.carousel');
        const items = document.querySelectorAll('.carousel-item');
        const prevBtn = document.getElementById('prev');
        const nextBtn = document.getElementById('next');

        let currentIndex = 0;

        function showItem(index) {
            items.forEach((item, i) => {
                item.style.transform = `translateX(${(i - currentIndex) * 100}%)`;
            });
        }

        function updateCarousel() {
            showItem(currentIndex);
        }

        prevBtn.addEventListener('click', () => {
            currentIndex = (currentIndex - 1 + items.length) % items.length;
            updateCarousel();
        });

        nextBtn.addEventListener('click', () => {
            currentIndex = (currentIndex + 1) % items.length;
            updateCarousel();
        });

        // Initialize carousel
        updateCarousel();
