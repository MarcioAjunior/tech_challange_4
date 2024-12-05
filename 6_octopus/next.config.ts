import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  reactStrictMode: true,

  i18n: {
    locales: ["en", "pt-BR"], 
    defaultLocale: "pt-BR",   
  },

  
  images: {
    domains: ["example.com"],
    formats: ["image/webp"],  
  },


  staticPageGenerationTimeout: 60, 
};

export default nextConfig;
