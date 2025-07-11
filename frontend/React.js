// React frontend
import { useState } from "react";
import axios from "axios";

export default function App() {
  const [file, setFile] = useState(null);
  const [kpis, setKpis] = useState(null);
  const [flags, setFlags] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!file) return;
    const formData = new FormData();
    formData.append("file", file);
    setLoading(true);
    const res = await axios.post("http://localhost:5000/analyze", formData);
    setKpis(res.data.kpis);
    setFlags(res.data.flags);
    setLoading(false);
  };

  return (
    <div className="p-6 max-w-xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">📑 Financial Statement Analyzer</h1>
      <input
        type="file"
        accept=".pdf"
        onChange={(e) => setFile(e.target.files[0])}
        className="mb-4"
      />
      <button
        onClick={handleSubmit}
        className="bg-blue-600 text-white px-4 py-2 rounded"
      >
        {loading ? "Analyzing..." : "Analyze PDF"}
      </button>

      {kpis && (
        <div className="mt-6">
          <h2 className="text-xl font-semibold mb-2">Extracted KPIs</h2>
          <table className="table-auto border w-full text-left">
            <thead>
              <tr><th className="border p-2">Metric</th><th className="border p-2">Value</th></tr>
            </thead>
            <tbody>
              {Object.entries(kpis).map(([key, value]) => (
                <tr key={key}><td className="border p-2">{key}</td><td className="border p-2">{value}</td></tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {flags && (
        <div className="mt-6">
          <h2 className="text-xl font-semibold mb-2">🚩 Red Flags</h2>
          <ul className="list-disc pl-5">
            {flags.map((f, i) => <li key={i}>{f}</li>)}
          </ul>
        </div>
      )}
    </div>
  );
}