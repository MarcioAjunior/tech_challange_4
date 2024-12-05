export async function POST(req: Request) {
    const { date } = await req.json();
  
    if (!date) {
      return new Response(
        JSON.stringify({ error: "Data não fornecida" }),
        { status: 400 }
      );
    }

    const apiUrl = process.env.NEXT_PUBLIC_API_MODEL;

    if (!apiUrl) {
      throw new Error("A variável de ambiente NEXT_PUBLIC_API_MODEL não está definida.");
    }
    
    const response = await fetch(apiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({"date" : date}), 
    });

    const predictions = await response.json()

    return new Response(
      JSON.stringify(predictions),
      { status: 200 }
    );
  }
  