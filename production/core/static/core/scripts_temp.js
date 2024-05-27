document.addEventListener('DOMContentLoaded', event => {
    const sidebarWrapper = document.getElementById('sidebar-wrapper');
    const menuToggle = document.body.querySelector('.menu-toggle');

    // ... your existing dropdown toggle code ...

    // Function to save sidebar state
    function saveSidebarState() {
        const isOpen = sidebarWrapper.classList.contains('active');
        localStorage.setItem('sidebarState', isOpen ? 'open' : 'closed');
    }

    // Function to restore sidebar state
    function restoreSidebarState() {
        const savedState = localStorage.getItem('sidebarState');
        if (savedState === 'open') {
            sidebarWrapper.classList.add('active');
            menuToggle.classList.add('active');
            _toggleMenuIcon(); 
        } 
    }

    // Event listener for menu toggle
    menuToggle.addEventListener('click', event => {
        // ... your existing menu toggle logic ...
        saveSidebarState(); // Save the new state after toggling
    });

    // Restore state on page load
    restoreSidebarState();

    // ... your existing scroll handlers and other code ...
});

// ... (fadeIn and fadeOut functions remain the same)
