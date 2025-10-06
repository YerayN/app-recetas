import React from "react";
import RecetaForm from "./RecetaForm";
import RecetasList from "./RecetasList";

export default function App() {
  return (
    <div className="min-h-screen bg-gray-100 text-gray-800 p-6">
          <div className="p-8 text-center bg-blue-100 text-blue-800 rounded-xl shadow-lg">
      <h1 className="text-3xl font-bold mb-2">🎨 Tailwind está funcionando</h1>
      <p className="text-gray-600">Si este bloque tiene color y bordes redondeados, todo está bien 😎</p>
    </div>

      {/* HEADER */}
      <header className="bg-indigo-600 text-white shadow-md">
        <div className="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
          <h1 className="text-2xl font-semibold tracking-wide">🍲 Recetas App</h1>
          <nav className="flex gap-4 text-sm opacity-90">
            <a href="#" className="hover:text-yellow-300 transition-colors">
              Inicio
            </a>
            <a href="#" className="hover:text-yellow-300 transition-colors">
              Mis Recetas
            </a>
            <a href="#" className="hover:text-yellow-300 transition-colors">
              Nueva Receta
            </a>
          </nav>
        </div>
      </header>

      {/* MAIN CONTENT */}
      <main className="max-w-6xl mx-auto px-6 py-10 grid md:grid-cols-2 gap-10">
        <section className="bg-white rounded-2xl shadow-md p-6">
          <h2 className="text-xl font-semibold mb-4 border-b pb-2">Crear Receta</h2>
          <RecetaForm />
        </section>

        <section className="bg-white rounded-2xl shadow-md p-6">
          <h2 className="text-xl font-semibold mb-4 border-b pb-2">Lista de Recetas</h2>
          <RecetasList />
        </section>
      </main>

      {/* FOOTER */}
      <footer className="bg-indigo-700 text-indigo-100 text-center py-3 mt-10 text-sm">
        © {new Date().getFullYear()} Recetas App — Creado por Yeray 🍳
      </footer>
    </div>
  );
}
