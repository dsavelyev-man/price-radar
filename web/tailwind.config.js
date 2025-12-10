// tailwind.config.js
import { heroui  } from "@heroui/react";

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./node_modules/@heroui/**/*.{js,ts,jsx,tsx}",

  ],
  theme: {
    extend: {},
  },
  darkMode: "class",
  plugins: [heroui()],
};