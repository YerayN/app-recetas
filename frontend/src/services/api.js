// src/services/api.js
const API_URL = "http://127.0.0.1:8000/api";

export async function getRecetas() {
  const response = await fetch(`${API_URL}/recetas/`);
  if (!response.ok) {
    throw new Error("Error al obtener las recetas");
  }
  return await response.json();
}
