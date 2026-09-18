document.addEventListener('DOMContentLoaded', () => {
    // Inicialização segura de Tooltips caso existam no documento
    if (typeof bootstrap !== 'undefined') {
        const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
        tooltipTriggerList.forEach(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));
    }

    console.log("Site recarregado com sucesso.");
});