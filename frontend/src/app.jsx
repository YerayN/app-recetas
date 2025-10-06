import { useState } from "react";
import RecetaForm from "./RecetaForm";
import RecetasList from "./RecetasList";

export default function App() {
  const [activeSection, setActiveSection] = useState("crear");

  return (
    <div className="min-h-screen bg-[#faf7f5] flex flex-col text-[#3f3d3b]">
      {/* Header */}
      <header className="bg-white border-b border-[#e9ded5] shadow-sm">
        <div className="max-w-3xl mx-auto px-5 py-4 flex justify-between items-center">
          <h1 className="text-2xl font-bold text-[#7a5af8] flex items-center gap-2">
            🍽️ Recetario
          </h1>
          <nav className="flex gap-6 text-sm font-medium text-[#7a5af8]">
            <button
              className={`transition-colors ${
                activeSection === "crear" ? "text-[#5b3cc4]" : "hover:text-[#5b3cc4]"
              }`}
              onClick={() => setActiveSection("crear")}
            >
              Nueva
            </button>
            <button
              className={`transition-colors ${
                activeSection === "lista" ? "text-[#5b3cc4]" : "hover:text-[#5b3cc4]"
              }`}
              onClick={() => setActiveSection("lista")}
            >
              Recetas
            </button>
          </nav>
        </div>
      </header>

      {/* Contenido */}
      <main className="flex-grow flex justify-center items-start">
        <div className="w-full max-w-md p-5">
          {activeSection === "crear" ? (
            <section className="bg-white rounded-2xl p-6 shadow-md border border-[#e9ded5]">
              <h2 className="text-lg font-semibold mb-4 text-[#4b3c2f] flex items-center gap-2">
                🧁 Nueva Receta
              </h2>
              <RecetaForm />
            </section>
          ) : (
            <section className="bg-white rounded-2xl p-6 shadow-md border border-[#e9ded5]">
              <h2 className="text-lg font-semibold mb-4 text-[#4b3c2f] flex items-center gap-2">
                📚 Tus Recetas
              </h2>
              <RecetasList />
            </section>
          )}
        </div>
      </main>

      {/* Footer */}
      <footer className="bg-white border-t border-[#e9ded5] py-4 text-center text-sm text-[#6b5e4e] opacity-70">
        © {new Date().getFullYear()} Recetario — Creado por Yeray
      </footer>
    </div>
  );
}
