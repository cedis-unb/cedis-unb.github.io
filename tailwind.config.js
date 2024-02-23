const defaultTheme = require('tailwindcss/defaultTheme');

// tailwind.config.js ajustado para melhor adequação visual
module.exports = {
  content: ['./layouts/**/*.html', './content/**/*.md'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        // Definições de cores principais baseadas na identidade visual
        primary: {
          DEFAULT: '#51C5CF', // Azul claro vibrante como cor primária
          50: '#E6F8FA', // Tons mais claros para gradientes e backgrounds
          100: '#CFF2F5',
          200: '#9DE4EA',
          300: '#6BD6DF',
          400: '#39C8D4',
          500: '#51C5CF', // DEFAULT
          600: '#1C9699', // Cor secundária mais escura para contraste
          700: '#14707A',
          800: '#0E4A5B',
          900: '#07243C',
        },
        secondary: {
          DEFAULT: '#F7941E', // Laranja para ações secundárias/acento
          50: '#FEF6E8', // Tons mais claros para gradientes e backgrounds
          100: '#FDECD2',
          200: '#FBDFAA',
          300: '#F9D183',
          400: '#F8C35B',
          500: '#F7941E', // DEFAULT
          600: '#D57818',
          700: '#B35C12',
          800: '#91410C',
          900: '#6E2606',
        },
        accent: {
          DEFAULT: '#E82C0C', // Vermelho para ações/acento principais
          50: '#FDE5E3', // Tons mais claros para gradientes e backgrounds
          100: '#FBC6C2',
          200: '#F88A86',
          300: '#F54E4A',
          400: '#F2120E',
          500: '#E82C0C', // DEFAULT
          600: '#C1260A',
          700: '#9A1F08',
          800: '#731806',
          900: '#4C1104',
        },
        // Ajuste de cores neutras para tipografia e backgrounds
        neutral: defaultTheme.colors.gray, // Usando a paleta padrão do Tailwind para neutros
      },
      lineHeight: {
        'extra-loose': '2.5',
        '12': '3rem',
      },
      typography: (theme) => ({
        DEFAULT: {
          css: {
            '--tw-prose-body': theme('colors.neutral.700'),
            '--tw-prose-headings': theme('colors.primary.900'),
            '--tw-prose-lead': theme('colors.primary.600'),
            '--tw-prose-links': theme('colors.primary.DEFAULT'),
            '--tw-prose-bold': theme('colors.primary.800'),
            '--tw-prose-counters': theme('colors.secondary.600'),
            '--tw-prose-bullets': theme('colors.accent.600'),
            '--tw-prose-hr': theme('colors.neutral.300'),
            '--tw-prose-quotes': theme('colors.secondary.800'),
            '--tw-prose-quote-borders': theme('colors.primary.300'),
            '--tw-prose-captions': theme('colors.neutral.700'),
            '--tw-prose-code': theme('colors.accent.DEFAULT'),
            '--tw-prose-pre-code': theme('colors.accent.700'),
            '--tw-prose-pre-bg': theme('colors.neutral.800'),
            '--tw-prose-th-borders': theme('colors.neutral.300'),
            '--tw-prose-td-borders': theme('colors.neutral.200'),
            '--tw-prose-invert-body': theme('colors.neutral.200'),
            '--tw-prose-invert-headings': theme('colors.white'),
            '--tw-prose-invert-lead': theme('colors.neutral.300'),
            '--tw-prose-invert-links': theme('colors.primary.200'),
            '--tw-prose-invert-bold': theme('colors.white'),
            '--tw-prose-invert-counters': theme('colors.secondary.400'),
            '--tw-prose-invert-bullets': theme('colors.accent.400'),
            '--tw-prose-invert-hr': theme('colors.neutral.500'),
            '--tw-prose-invert-quotes': theme('colors.secondary.100'),
            '--tw-prose-invert-quote-borders': theme('colors.primary.500'),
            '--tw-prose-invert-captions': theme('colors.neutral.400'),
            '--tw-prose-invert-code': theme('colors.accent.300'),
            '--tw-prose-invert-pre-code': theme('colors.accent.500'),
            '--tw-prose-invert-pre-bg': theme('colors.neutral.900'),
          },
        },
      }),
    },
  },
  variants: {
    extend: {
      typography: ['dark'],
    },
  },
  plugins: [require('@tailwindcss/typography')],
};
