import { useState } from 'react';
import UnitsSelect from './components/UnitsSelect';

export default function App() {
  const [unitId, setUnitId] = useState(null);

  return (
    <div style={{ maxWidth: 680, margin: '2rem auto', fontFamily: 'system-ui, sans-serif' }}>
      <h1 style={{ fontSize: 24, fontWeight: 700, marginBottom: 16 }}>Recetas App — Paso 1</h1>

      <label style={{ display: 'block', marginBottom: 8, fontWeight: 600 }}>
        Unidad
      </label>
      <UnitsSelect value={unitId} onChange={setUnitId} />

      <p style={{ marginTop: 16 }}>
        Unidad seleccionada: <strong>{unitId ?? '—'}</strong>
      </p>
    </div>
  );
}
