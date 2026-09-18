document.addEventListener('DOMContentLoaded', () => {

    // 1. Inicialização de Tooltips do Bootstrap (com checagem de segurança)
    if (typeof bootstrap !== 'undefined') {
        const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
        tooltipTriggerList.forEach(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));
    }

    // 2. Validação condicional do Formulário (apenas executa se o formulário existir na página)
    const formContato = document.querySelector('form');
    if (formContato) {
        formContato.addEventListener('submit', (event) => {
            event.preventDefault();
            const nome = document.getElementById('nome')?.value.trim();
            if (nome) {
                alert(`Obrigado pelo seu contacto, ${nome}!`);
                formContato.reset();
            }
        });
    }

    console.log("Projeto Web carregado com sucesso sem erros.");
});