import React, { useState } from "react";
import Dashboard from "./components/Dashboard";

function App() {
  const [output, setOutput] = useState("");
  const [imageData, setImageData] = useState(null);
  const [showGraph, setShowGraph] = useState(false);
  const fetchData = async (url, body) => {
    const response = await fetch("http://127.0.0.1:8000/" + url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });
    return await response.json();
  };


  // ===== Handlers =====

  const callRoute = async (route, body, key = "result") => {
    fetchData(route, body)
      .then((data) => {
        console.log("data:", data);
        if (data.iterations) {
          setOutput(data.iterations.join("\n"));
        } else if (data.condition_number) {
          setOutput(`Condition Number: ${data.condition_number}`);
        } else {
          setOutput(data[key] ?? JSON.stringify(data));
        }
        if (data.plot_base64) {
          setImageData(data.plot_base64); // Save the base64 image
        }
        else {
          setImageData(null); // Clear the image if no plot is returned
        }
      })
      .catch((error) => {
        console.error("Error:", error);
        setOutput("Error: " + error.message);
      });
  };

  return (
    <>
      <Dashboard onClick={callRoute} output={output} />
      {imageData && (
        <button onClick={() => setShowGraph(!showGraph)} style={{ margin: "10px", padding: "5px 10px" }}>
          {showGraph ? "הסתר גרף" : "הצג גרף"}
        </button>
      )}
      <br />
      {imageData && showGraph && (
        <img
          src={`data:image/png;base64,${imageData}`}
          alt="Generated Plot"
          style={{ maxWidth: "500px", border: "1px solid #ccc" }}
        />
      )}
    </>
  );
}

export default App;
