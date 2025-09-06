// tailwind.config.js
export default {
    content: [
      "./app/**/*.{vue,js,ts}",
      "./components/**/*.{vue,js,ts}",
      "./pages/**/*.{vue,js,ts}"
    ],
    theme: {
      extend: {
        colors: {
          primary: {
            50: '#eef2ff',
            100: '#e0e7ff',
            200: '#c7d2fe',
            300: '#a5b4fc',
            400: '#818cf8',
            500: '#6366f1',  // main
            600: '#4f46e5',  // hover
            700: '#4338ca',
            800: '#3730a3',
            900: '#312e81',
          },
          secondary: {
            500: '#ec4899', // example
            600: '#db2777',
          }
        }
      }
    },
    plugins: [],
  }
  