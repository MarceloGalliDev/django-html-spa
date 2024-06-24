document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        // Esconder a tela de carregamento
        const loadingScreen = document.getElementById('loading-screen');
        loadingScreen.style.transition = 'opacity 1s';
        loadingScreen.style.opacity = '0';
        setTimeout(function() {
            loadingScreen.style.display = 'none';
        }, 1000);

        // Mostrar o conteúdo principal
        const mainContent = document.getElementById('main-content');
        mainContent.style.display = 'flex';
        mainContent.style.transition = 'opacity 1s';
        mainContent.style.opacity = '1';
    }, 1500);
});
