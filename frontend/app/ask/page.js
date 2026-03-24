"use client"
import { useState } from "react";

export default function AskPage() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();
    const res = await fetch("http://localhost:8000/ask", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "x-api-key": "secret-key-123"
      },
      body: JSON.stringify({ question })
    });
    const data = await res.json();
    setAnswer(data.answer);
  }

  return (
    <main className="p-8">
      <h1 className="text-2xl font-bold mb-4">Ask</h1>
      <form onSubmit={handleSubmit} className="flex flex-col gap-4">
        <input
            className="border p-2 rounded"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Ask a question..."
        />
        <button type="submit" className="bg-blue-500 text-white rounded p-2">Submit</button>
      </form>
        {answer && <p className="mt-4">{answer}</p>}
    </main>
  );


}