import { useState } from 'react';
import UnitsSelect from './components/UnitsSelect';

import IngredienteAutocomplete from "./components/IngredienteAutocomplete";

function App() {
  const [ingrediente, setIngrediente] = useState(null);

  return (
    <div className="p-6 max-w-lg mx-auto">
      <h1 className="text-2xl font-bold mb-4">Prueba de Autocompletado</h1>
      <IngredienteAutocomplete
        value={ingrediente}
        onChange={(i) => setIngrediente(i)}
      />
      {ingrediente && (
        <div className="mt-4 text-sm text-gray-600">
          Seleccionado: <b>{ingrediente.nombre}</b> (id {ingrediente.id})
        </div>
      )}
    </div>
  );
}

export default App;

