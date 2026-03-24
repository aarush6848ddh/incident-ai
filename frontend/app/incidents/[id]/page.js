export default async function IncidentDetail({ params }) {
    const { id } = await params
    const res = await fetch(`http://api:8000/incidents`, {
        headers: { "x-api-key": "secret-key-123" }
    })
    const incidents = await res.json()
    const incident = incidents.find(i => i.id === Number(id))

    return (
        <main className="p-8">
            <h1 className="text-2xl font-bold mb-4">{incident.title}</h1>
            <p>Severity: {incident.severity}</p>
            <p>Status: {incident.status}</p>
            <p>Description: {incident.description}</p>
        </main>
    )   
}
