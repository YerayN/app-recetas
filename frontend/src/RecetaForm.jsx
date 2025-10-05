import { useState, useEffect } from "react";
import { createReceta, updateReceta } from "./services/api";

export default function RecetaForm({ recetaActual, onSaved, onCancel }) {
  const [form, setForm] = useState({
    nombre: "",
    descripcion: "",
    tiempo_preparacion: "",
    instrucciones: "",
    ingredientes: [],
  });
  const [error, setError] = useState(null);

  // 🧠 Si estamos editando, rellenamos el formulario con los datos actuales
  useEffect(() => {
    if (recetaActual) {
      setForm({
        nombre: recetaActual.nombre || "",
        descripcion: recetaActual.descripcion || "",
        tiempo_preparacion: recetaActual.tiempo_preparacion || "",
        instrucciones: recetaActual.instrucciones || "",
        ingredientes: recetaActual.ingredientes || [],
      });
    } else {
      setForm({
        nombre: "",
        descripcion: "",
        tiempo_preparacion: "",
        instrucciones: "",
        ingredientes: [],
      });
    }
  }, [recetaActual]);

  // 🧱 Manejadores generales
  function handleChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  function handleIngredienteChange(index, field, value) {
    const nuevos = [...form.ingredientes];
    nuevos[index][field] = value;
    setForm({ ...form, ingredientes: nuevos });
  }

  function agregarIngrediente() {
    setForm({
      ...form,
      ingredientes: [...form.ingredientes, { nombre: "", cantidad: "", unidad: "" }],
    });
  }

  function eliminarIngrediente(index) {
    const nuevos = form.ingredientes.filter((_, i) => i !== index);
    setForm({ ...form, ingredientes: nuevos });
  }

  async function handleSubmit(e) {
    e.preventDefault();
    try {
      const payload = {
        ...form,
        tiempo_preparacion: parseInt(form.tiempo_preparacion) || 0,
        ingredientes: form.ingredientes.map((ing) => ({
          ...ing,
          cantidad: parseFloat(ing.cantidad) || 0,
        })),
      };

      if (recetaActual) {
        await updateReceta(recetaActual.id, payload);
      } else {
        await createReceta(payload);
      }

      onSaved();
    } catch (err) {
      setError(err.message);
    }
  }

  // 🧾 Renderizado
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

      <h3>Ingredientes</h3>
      {form.ingredientes.map((ing, index) => (
        <div key={index} style={{ marginBottom: "0.5rem" }}>
          <input
            placeholder="Nombre"
            value={ing.nombre}
            onChange={(e) => handleIngredienteChange(index, "nombre", e.target.value)}
            style={{ width: "40%" }}
          />
          <input
            placeholder="Cantidad"
            type="number"
            value={ing.cantidad}
            onChange={(e) => handleIngredienteChange(index, "cantidad", e.target.value)}
            style={{ width: "20%", marginLeft: "0.5rem" }}
          />
          <input
            placeholder="Unidad"
            value={ing.unidad}
            onChange={(e) => handleIngredienteChange(index, "unidad", e.target.value)}
            style={{ width: "20%", marginLeft: "0.5rem" }}
          />
          <button
            type="button"
            onClick={() => eliminarIngrediente(index)}
            style={{ marginLeft: "0.5rem", color: "red" }}
          >
            ✕
          </button>
        </div>
      ))}

      <button type="button" onClick={agregarIngrediente}>
        + Añadir ingrediente
      </button>

      <br />
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
