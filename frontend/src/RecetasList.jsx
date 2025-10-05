import { useEffect, useState } from "react";
import { getRecetas, deleteReceta } from "./services/api";
import RecetaForm from "./RecetaForm";

export default function RecetasList() {
  const [recetas, setRecetas] = useState([]);
  const [error, setError] = useState(null);
  const [recetaEditando, setRecetaEditando] = useState(null);

  async function cargarRecetas() {
    try {
      const data = await getRecetas();
      setRecetas(data);
      setRecetaEditando(null);
    } catch (err) {
      setError(err.message);
    }
  }

  async function handleEliminar(id) {
    const confirmar = window.confirm("¿Seguro que deseas eliminar esta receta?");
    if (!confirmar) return;

    try {
      await deleteReceta(id);
      await cargarRecetas();
    } catch (err) {
      alert("Error al eliminar la receta: " + err.message);
    }
  }

  useEffect(() => {
    cargarRecetas();
  }, []);

  if (error) return <p>Error: {error}</p>;

  return (
    <div style={{ padding: "1rem" }}>
      <h1>📖 Recetas</h1>

      <RecetaForm
        recetaActual={recetaEditando}
        onSaved={cargarRecetas}
        onCancel={() => setRecetaEditando(null)}
      />

      {recetas.length === 0 ? (
        <p>No hay recetas todavía.</p>
      ) : (
        <ul>
          {recetas.map((receta) => (
            <li key={receta.id} style={{ marginBottom: "1rem" }}>
              <strong>{receta.nombre}</strong> — {receta.tiempo_preparacion} min
              <br />
              <small>{receta.descripcion}</small>
              <br />
              <button onClick={() => setRecetaEditando(receta)}>Editar</button>
              <button
                onClick={() => handleEliminar(receta.id)}
                style={{ marginLeft: "0.5rem", color: "red" }}
              >
                Eliminar
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
