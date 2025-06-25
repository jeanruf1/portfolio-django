// backend/theme/static_src/tailwind.config.js

const theme = require('tailwindcss/defaultTheme')

module.exports = {
    /**
     * O array 'content' diz ao Tailwind para escanear todos os arquivos .html
     * dentro de qualquer pasta de templates no nosso projeto para encontrar as
     * classes de estilo que usamos.
     */
    content: [
        '../../templates/**/*.html',
        '../../**/templates/**/*.html',
    ],

    /**
     * A seção 'theme' é onde customizamos o design.
     */
    theme: {
        extend: {
            // Aqui estamos adicionando nossas fontes customizadas do Google Fonts.
            fontFamily: {
                // Classe 'font-sans' usará 'Inter'.
                sans: ['Inter', ...theme.fontFamily.sans],
                // Classe 'font-serif' usará 'Lora'.
                serif: ['Lora', ...theme.fontFamily.serif],
            },
        },
    },

    /**
     * A seção 'plugins' adiciona funcionalidades extras ao Tailwind.
     * Estes são úteis para formulários, tipografia e proporção de vídeo.
     */
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}