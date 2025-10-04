import { useState } from "react";
import { createReceta } from "./services/api";

export default function RecetaForm({ onCreated }) {
  const [form, setForm] = useState({
    nombre: "",
    descripcion: "",
    tiempo_preparacion: "",
    instrucciones: "",
    ingredientes: "",
  });
  const [error, setError] = useState(null);

  function handleChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  async function handleSubmit(e) {
    e.preventDefault();
    try {
      await createReceta({
        ...form,
        tiempo_preparacion: parseInt(form.tiempo_preparacion),
      });
      setForm({
        nombre: "",
        descripcion: "",
        tiempo_preparacion: "",
        instrucciones: "",
        ingredientes: "",
      });
      onCreated(); // actualizar lista en RecetasList
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <form onSubmit={handleSubmit} style={{ marginBottom: "2rem" }}>
      <h2>Nueva receta</h2>
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

      <textarea
        name="ingredientes"
        placeholder="Ingredientes"
        value={form.ingredientes}
        onChange={handleChange}
      />
      <br />

      <button type="submit">Guardar receta</button>
    </form>
  );
}
