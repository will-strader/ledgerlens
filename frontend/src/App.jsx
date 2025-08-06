import { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [kpis, setKpis] = useState(null);
  const [flags, setFlags] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!file) return;
    const formData = new FormData();
    formData.append("file", file);
    setLoading(true);
    const res = await axios.post("https://ledgerlens.onrender.com/analyze", formData);
    setKpis(res.data.kpis);
    setFlags(res.data.flags);
    setLoading(false);
  };

  return (
    <div style={{ padding: "2rem", maxWidth: "800px", margin: "auto" }}>
      <h1> LedgerLens: Financial Statement Analyzer</h1>
      <input type="file" accept=".pdf" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleSubmit} style={{ marginLeft: "1rem" }}>
        {loading ? "Analyzing..." : "Analyze PDF"}
      </button>

      {kpis && (
        <div>
          <h2>Extracted KPIs</h2>
          <ul>
            {Object.entries(kpis).map(([k, v]) => (
              <li key={k}>
                <strong>{k}:</strong> {v}
              </li>
            ))}
          </ul>
        </div>
      )}

      {flags && (
        <div>
          <h2>🚩 Red Flags</h2>
          <ul>
            {flags.map((f, i) => (
              <li key={i}>{f}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;