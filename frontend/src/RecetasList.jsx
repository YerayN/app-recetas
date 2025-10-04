import { useEffect, useState } from "react";
import { getRecetas } from "./services/api";

export default function RecetasList() {
  const [recetas, setRecetas] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    getRecetas()
      .then(data => setRecetas(data))
      .catch(err => setError(err.message));
  }, []);

  if (error) return <p>Error: {error}</p>;
  if (!recetas.length) return <p>Cargando recetas...</p>;

  return (
    <div style={{ padding: "1rem" }}>
      <h1>📖 Recetas</h1>
      <ul>
        {recetas.map(receta => (
          <li key={receta.id}>
            <strong>{receta.nombre}</strong> — {receta.tiempo_preparacion} min
            <br />
            <small>{receta.descripcion}</small>
          </li>
        ))}
      </ul>
    </div>
  );
}
