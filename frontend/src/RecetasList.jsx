import { useEffect, useState } from "react";
import { getRecetas } from "./services/api";
import RecetaForm from "./RecetaForm";

export default function RecetasList() {
  const [recetas, setRecetas] = useState([]);
  const [error, setError] = useState(null);

  async function cargarRecetas() {
    try {
      const data = await getRecetas();
      setRecetas(data);
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
      <RecetaForm onCreated={cargarRecetas} />
      {recetas.length === 0 ? (
        <p>No hay recetas todavía.</p>
      ) : (
        <ul>
          {recetas.map((receta) => (
            <li key={receta.id}>
              <strong>{receta.nombre}</strong> — {receta.tiempo_preparacion} min
              <br />
              <small>{receta.descripcion}</small>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
