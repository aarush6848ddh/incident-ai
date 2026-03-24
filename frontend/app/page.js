import Link from "next/link";

export default async function Home() { 
  const res = await fetch("http://api:8000/incidents", {
  headers: {
    "x-api-key": "secret-key-123"
  }
  });
  const incidents = await res.json();

  return (
    <main className="p-8">
      <h1 className="text-2xl font-bold mb-4">Incident</h1>
      <div className="flex flex-col gap-4">
        {incidents.map((incident) => (
          <Link key={incident.id} href={`/incidents/${incident.id}`}>  
            <div className="p-4 border rounded hover:bg-gray-100">
              <h2>{incident.title}</h2>
              <p>{incident.severity}</p>
              <p>{incident.status}</p>
            </div>
          </Link>
        ))}
      </div>
    </main>

                                                                 
  ); 

}
