import { useEffect, useState } from "react";
import { getRecetas } from "./services/api";
import RecetaForm from "./RecetaForm";

export default function RecetasList() {
  const [recetas, setRecetas] = useState([]);
  const [error, setError] = useState(null);
  const [recetaEditando, setRecetaEditando] = useState(null);

  async function cargarRecetas() {
    try {
      const data = await getRecetas();
      setRecetas(data);
      setRecetaEditando(null); // salimos del modo edición tras guardar
    } catch (err) {
      setError(err.message);
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
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
