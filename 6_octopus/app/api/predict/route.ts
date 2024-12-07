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
    
    console.log('BBBBBBBBBBBBBBBBBBBBB')
    console.log(date)


    const response = await fetch(apiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({"date" : date}), 
    });

    console.log('CCCCCCCCCCCCCCCCCCCCCCCCCC')
    console.log(response)


    const predictions = await response.json()

    return new Response(
      JSON.stringify(predictions),
      { status: 200 }
    );
  }
  