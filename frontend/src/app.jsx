import { useState, useEffect } from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link,
  useNavigate,
  useLocation,
} from "react-router-dom";
import RecetaForm from "./RecetaForm";
import RecetasList from "./RecetasList";
import RecetaDetalle from "./RecetaDetalle";
import {
  HomeIcon,
  BookOpenIcon,
  PlusCircleIcon,
  CalendarIcon,
  ShoppingCartIcon,
} from "@heroicons/react/24/outline";

const API = "http://127.0.0.1:8000/api"; // 👈 unifica aquí


function AppContent() {
  const [recetas, setRecetas] = useState([]);
  const navigate = useNavigate();
  const { pathname } = useLocation();

  // 🧾 Cargar recetas desde el backend
  const fetchRecetas = async () => {
    try {
      const res = await fetch(`${API}/recetas/`);      
      if (!res.ok) throw new Error("Error al cargar recetas");
      const data = await res.json();
      setRecetas(data);
    } catch (error) {
      console.error("Error cargando recetas:", error);
    }
  };

  useEffect(() => {
    fetchRecetas();
  }, []);

  // 🧁 Crear receta
  const handleCreate = async (formData) => {
    try {
      const res = await fetch(`${API}/recetas/`, {
        method: "POST",
        body: formData,
      });

      // Intenta leer el json aunque no sea 200
      const data = await res.json().catch(() => ({}));

      if (!res.ok) {
        console.error("POST /recetas/ error:", data);
        const msg =
          typeof data === "object" && data
            ? Object.entries(data)
                .map(([k, v]) => `${k}: ${Array.isArray(v) ? v.join(", ") : v}`)
                .join("\n")
            : "Error al guardar receta";
        alert(`❌ ${msg}`);
        return;
      }

      // DRF suele devolver el objeto creado. Lo añadimos o recargamos todo:
      // setRecetas(prev => [data, ...prev]); // opción rápida
      await fetchRecetas(); // opción consistente

      navigate("/recetas");
    } catch (error) {
      console.error("Error al crear receta:", error);
      alert("❌ Error de conexión con el servidor");
    }
  };


  return (
    <div className="min-h-screen bg-[#FAF8F6] text-gray-800 flex flex-col font-['Inter'] pb-20 md:pb-0">
      {/* HEADER */}
<header className="w-full border-b border-gray-200 bg-[#FAF8F6]/70 backdrop-blur-md sticky top-0 z-10">
  <div className="max-w-6xl mx-auto px-4 py-4 flex justify-between items-center">
    <h1 className="text-xl font-semibold text-[#8B5CF6]">
      <Link to="/">Recetas App</Link>
    </h1>

    {/* Menú principal (solo visible en escritorio) */}
    <nav className="hidden md:flex gap-6 text-sm font-medium">
      <Link to="/" className="hover:text-[#8B5CF6] transition-colors">
        Inicio
      </Link>
      <Link
        to="/recetas"
        className="hover:text-[#8B5CF6] transition-colors"
      >
        Mis recetas
      </Link>
      <Link
        to="/recetas/nueva"
        className="hover:text-[#8B5CF6] transition-colors"
      >
        Nueva receta
      </Link>
      <Link
        to="/plan-semanal"
        className="hover:text-[#8B5CF6] transition-colors"
      >
        Plan semanal
      </Link>
      <Link
        to="/lista"
        className="hover:text-[#8B5CF6] transition-colors"
      >
        Lista
      </Link>
    </nav>
  </div>
</header>


      {/* CONTENIDO DE LAS RUTAS */}
      <main className="flex-grow">
        <Routes>
          {/* PÁGINA PRINCIPAL */}
          <Route
            path="/"
            element={
              <section className="text-center mt-12 px-6">
                <h2 className="text-3xl md:text-4xl font-semibold mb-3 text-gray-800">
                  Tu cocina, organizada a tu ritmo 🍃
                </h2>
                <p className="text-gray-500 max-w-md mx-auto">
                  Planifica tus comidas, guarda tus recetas y genera tu lista de
                  la compra en un solo lugar.
                </p>

                {/* Tarjetas del dashboard */}
                <div className="max-w-6xl mx-auto px-4 py-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
                  <div className="bg-white rounded-2xl shadow-sm hover:shadow-md transition p-6 flex flex-col justify-between">
                    <div>
                      <h3 className="font-semibold text-lg mb-2 text-[#8B5CF6]">
                        Plan semanal
                      </h3>
                      <p className="text-sm text-gray-500 mb-4">
                        Organiza tus comidas de la semana fácilmente.
                      </p>
                    </div>
                    <button className="bg-[#8B5CF6] text-white py-2 rounded-lg text-sm hover:bg-[#7C3AED] transition">
                      Ver planificación
                    </button>
                  </div>

                  <div className="bg-white rounded-2xl shadow-sm hover:shadow-md transition p-6 flex flex-col justify-between">
                    <div>
                      <h3 className="font-semibold text-lg mb-2 text-[#8B5CF6]">
                        Mis recetas
                      </h3>
                      <p className="text-sm text-gray-500 mb-4">
                        Accede a tus recetas guardadas o crea una nueva.
                      </p>
                    </div>
                    <Link
                      to="/recetas"
                      className="text-center bg-[#A8BDA8] text-white py-2 rounded-lg text-sm hover:bg-[#94AD94] transition"
                    >
                      Ver recetas
                    </Link>
                  </div>

                  <div className="bg-white rounded-2xl shadow-sm hover:shadow-md transition p-6 flex flex-col justify-between">
                    <div>
                      <h3 className="font-semibold text-lg mb-2 text-[#8B5CF6]">
                        Lista de la compra
                      </h3>
                      <p className="text-sm text-gray-500 mb-4">
                        Genera automáticamente tu lista según el plan semanal.
                      </p>
                    </div>
                    <button className="bg-[#8B5CF6] text-white py-2 rounded-lg text-sm hover:bg-[#7C3AED] transition">
                      Generar lista
                    </button>
                  </div>

                  <div className="bg-white rounded-2xl shadow-sm hover:shadow-md transition p-6 sm:col-span-2 lg:col-span-3">
                    <h3 className="font-semibold text-lg mb-2 text-[#8B5CF6]">
                      Recomendaciones
                    </h3>
                    <p className="text-gray-600 text-sm">
                      🍔 Has planificado 3 comidas con alto contenido en grasas
                      esta semana. ¿Qué tal añadir un plato más ligero? 🌿
                    </p>
                  </div>
                </div>
              </section>
            }
          />

          {/* LISTA DE RECETAS */}
          <Route path="/recetas" element={<RecetasList recetas={recetas} />} />

          {/* FORMULARIO NUEVA RECETA */}
          <Route
            path="/recetas/nueva"
            element={<RecetaForm onSubmit={handleCreate} onUpdate={fetchRecetas} />}
          />

          {/* DETALLES DE RECETA */}
          <Route
            path="/recetas/:id"
            element={<RecetaDetalle onDelete={fetchRecetas} />}
          />

          {/* EDITAR RECETA */}
          <Route
            path="/recetas/:id/editar"
            element={<RecetaForm modo="editar" onUpdate={fetchRecetas} />}
          />


          </Routes>

      </main>

      {/* NAV INFERIOR (solo móvil) */}
      <nav className="md:hidden fixed bottom-0 left-0 right-0 bg-white border-t border-gray-200 flex justify-around items-center py-2 z-50 shadow-md">
        {/* 🏠 Inicio */}
        <Link
          to="/"
          className={`flex flex-col items-center text-xs transition-colors ${
            pathname === "/"
              ? "text-[#8B5CF6]"
              : "text-gray-600 hover:text-[#8B5CF6]"
          }`}
        >
          <div
            className={`p-2 rounded-full ${
              pathname === "/" ? "bg-[#8B5CF6]/10" : ""
            }`}
          >
            <HomeIcon className="w-6 h-6 mb-1" />
          </div>
          Inicio
        </Link>

        {/* 📘 Recetas */}
        <Link
          to="/recetas"
          className={`flex flex-col items-center text-xs transition-colors ${
            pathname === "/recetas" || /^\/recetas\/\d+$/.test(pathname)
              ? "text-[#8B5CF6]"
              : "text-gray-600 hover:text-[#8B5CF6]"
          }`}
        >
          <div
            className={`p-2 rounded-full ${
              pathname === "/recetas" || /^\/recetas\/\d+$/.test(pathname)
                ? "bg-[#8B5CF6]/10"
                : ""
            }`}
          >
            <BookOpenIcon className="w-6 h-6 mb-1" />
          </div>
          Recetas
        </Link>

        {/* ➕ Nueva */}
        <Link
          to="/recetas/nueva"
          className={`flex flex-col items-center text-xs transition-colors ${
            pathname === "/recetas/nueva"
              ? "text-[#8B5CF6]"
              : "text-gray-600 hover:text-[#8B5CF6]"
          }`}
        >
          <div
            className={`p-2 rounded-full ${
              pathname === "/recetas/nueva" ? "bg-[#8B5CF6]/10" : ""
            }`}
          >
            <PlusCircleIcon className="w-6 h-6 mb-1" />
          </div>
          Nueva
        </Link>

        {/* 📅 Plan */}
        <Link
          to="/plan-semanal"
          className={`flex flex-col items-center text-xs transition-colors ${
            pathname.startsWith("/plan-semanal")
              ? "text-[#8B5CF6]"
              : "text-gray-600 hover:text-[#8B5CF6]"
          }`}
        >
          <div
            className={`p-2 rounded-full ${
              pathname.startsWith("/plan-semanal") ? "bg-[#8B5CF6]/10" : ""
            }`}
          >
            <CalendarIcon className="w-6 h-6 mb-1" />
          </div>
          Plan
        </Link>

        {/* 🛒 Lista */}
        <Link
          to="/lista"
          className={`flex flex-col items-center text-xs transition-colors ${
            pathname.startsWith("/lista")
              ? "text-[#8B5CF6]"
              : "text-gray-600 hover:text-[#8B5CF6]"
          }`}
        >
          <div
            className={`p-2 rounded-full ${
              pathname.startsWith("/lista") ? "bg-[#8B5CF6]/10" : ""
            }`}
          >
            <ShoppingCartIcon className="w-6 h-6 mb-1" />
          </div>
          Lista
        </Link>
      </nav>


      {/* FOOTER */}
      <footer className="hidden md:block border-t border-gray-200 text-center py-3 text-sm text-gray-500 mt-auto">
        © {new Date().getFullYear()} Yeray Navarro · Recetas App
      </footer>
    </div>
  );
}

export default function App() {
  return (
    <Router>
      <AppContent />
    </Router>
  );
}
