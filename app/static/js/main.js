document.addEventListener('DOMContentLoaded', function() {
    // File input handling
    const fileInput = document.getElementById('file');
    const fileNameDisplay = document.querySelector('.file-name');
    
    fileInput.addEventListener('change', function() {
        if (this.files.length > 0) {
            fileNameDisplay.textContent = this.files[0].name;
        } else {
            fileNameDisplay.textContent = 'No file selected';
        }
    });
    
    // Form submission loading state
    const form = document.querySelector('.upload-form');
    const submitButton = document.querySelector('.submit-button');
    
    if (form) {
        form.addEventListener('submit', function() {
            submitButton.classList.add('loading');
        });
    }
    
    // Tab functionality for results page
    const tabButtons = document.querySelectorAll('.tab-button');
    
    tabButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Remove active class from all buttons and content
            document.querySelectorAll('.tab-button').forEach(btn => {
                btn.classList.remove('active');
            });
            
            document.querySelectorAll('.tab-content').forEach(content => {
                content.classList.remove('active');
            });
            
            // Add active class to clicked button and corresponding content
            this.classList.add('active');
            const tabName = this.getAttribute('data-tab');
            document.querySelector(`.tab-content[data-tab="${tabName}"]`).classList.add('active');
        });
    });
    
    // Animate elements as they come into view
    const animateOnScroll = function() {
        const elements = document.querySelectorAll('.animate__animated');
        
        elements.forEach(element => {
            const elementPosition = element.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;
            
            if (elementPosition < windowHeight - 100) {
                const animationClass = element.classList.item(1); // Get the animation class
                element.classList.add(animationClass);
            }
        });
    };
    
    window.addEventListener('scroll', animateOnScroll);
    animateOnScroll(); // Run once on page load
});