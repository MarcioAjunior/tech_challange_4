import axios from "axios";

const apiClient = axios.create({
  baseURL: "/api", // Base URL para chamadas internas no Next.js
});

export default apiClient;

//
