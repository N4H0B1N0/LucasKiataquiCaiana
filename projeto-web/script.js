// Aguarda o carregamento completo do DOM
document.addEventListener('DOMContentLoaded', () => {

    // 1. Inicialização do Tooltip do Bootstrap (se utilizado no projeto)
    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));

    // 2. Validação simples do Formulário de Contacto
    const formContato = document.querySelector('form');
    
    if (formContato) {
        formContato.addEventListener('submit', (event) => {
            event.preventDefault(); // Impede o envio padrão da página

            const nome = document.getElementById('nome').value.trim();
            const email = document.getElementById('email').value.trim();
            const mensagem = document.getElementById('mensagem').value.trim();

            if (nome === '' || email === '' || mensagem === '') {
                alert('Por favor, preencha todos os campos obrigatórios.');
                return;
            }

            // Exibe mensagem de sucesso visual
            alert(`Obrigado pelo seu contacto, ${nome}! A sua mensagem foi enviada com sucesso.`);
            
            // Limpa o formulário
            formContato.reset();
        });
    }

    // 3. Log de navegação ativa (Opcional)
    console.log("Projeto Web carregado com sucesso.");
});