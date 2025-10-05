import { useState, useEffect } from "react";
import { createReceta, updateReceta } from "./services/api";

export default function RecetaForm({ recetaActual, onSaved, onCancel }) {
  const [form, setForm] = useState({
    nombre: "",
    descripcion: "",
    tiempo_preparacion: "",
    instrucciones: "",
  });
  const [error, setError] = useState(null);

  // Rellenar el formulario si estamos editando
  useEffect(() => {
    if (recetaActual) {
      setForm({
        nombre: recetaActual.nombre,
        descripcion: recetaActual.descripcion,
        tiempo_preparacion: recetaActual.tiempo_preparacion,
        instrucciones: recetaActual.instrucciones,
      });
    }
  }, [recetaActual]);

  function handleChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  async function handleSubmit(e) {
    e.preventDefault();
    try {
      if (recetaActual) {
        // Modo edición
        await updateReceta(recetaActual.id, {
          ...form,
          tiempo_preparacion: parseInt(form.tiempo_preparacion),
        });
      } else {
        // Modo creación
        await createReceta({
          ...form,
          tiempo_preparacion: parseInt(form.tiempo_preparacion),
          ingredientes: [], // por ahora vacío
        });
      }
      setForm({
        nombre: "",
        descripcion: "",
        tiempo_preparacion: "",
        instrucciones: "",
      });
      onSaved();
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <form onSubmit={handleSubmit} style={{ marginBottom: "2rem" }}>
      <h2>{recetaActual ? "Editar receta" : "Nueva receta"}</h2>
      {error && <p style={{ color: "red" }}>{error}</p>}

      <input
        name="nombre"
        placeholder="Nombre"
        value={form.nombre}
        onChange={handleChange}
        required
      />
      <br />

      <input
        name="descripcion"
        placeholder="Descripción"
        value={form.descripcion}
        onChange={handleChange}
      />
      <br />

      <input
        name="tiempo_preparacion"
        type="number"
        placeholder="Tiempo (min)"
        value={form.tiempo_preparacion}
        onChange={handleChange}
      />
      <br />

      <textarea
        name="instrucciones"
        placeholder="Instrucciones"
        value={form.instrucciones}
        onChange={handleChange}
      />
      <br />

      <button type="submit">
        {recetaActual ? "Guardar cambios" : "Crear receta"}
      </button>
      {recetaActual && (
        <button type="button" onClick={onCancel} style={{ marginLeft: "1rem" }}>
          Cancelar
        </button>
      )}
    </form>
  );
}
