// src/services/api.js
const API_URL = "http://127.0.0.1:8000/api";

export async function getRecetas() {
  const response = await fetch(`${API_URL}/recetas/`);
  if (!response.ok) throw new Error("Error al obtener las recetas");
  return await response.json();
}

export async function createReceta(data) {
  const response = await fetch(`${API_URL}/recetas/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  if (!response.ok) throw new Error("Error al crear la receta");
  return await response.json();
}

export async function updateReceta(id, data) {
  const response = await fetch(`${API_URL}/recetas/${id}/`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  if (!response.ok) throw new Error("Error al actualizar la receta");
  return await response.json();
}

export async function deleteReceta(id) {
  const response = await fetch(`${API_URL}/recetas/${id}/`, {
    method: "DELETE",
  });
  if (!response.ok) throw new Error("Error al eliminar la receta");
  return true;
}
