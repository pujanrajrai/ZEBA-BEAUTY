/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        primary: "#0D76B8",
        formcolor: "#F1FAFE",
        secondary: "#F45115",
        slateblue: "#E7F4FC",
        background: "#f8f9fc",
      },
      fontFamily: {
        sans: ["Poppins", "Proxima Nova", "sans-serif"], // Set Poppins as the default sans-serif font
      },

    },
  },
  plugins: [],
}

