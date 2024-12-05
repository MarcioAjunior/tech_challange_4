import { NextResponse } from 'next/server';

export async function GET() {
  try {
    
    const apiUrl = process.env.NEXT_PUBLIC_API_METRICS;

    if (!apiUrl) {
      throw new Error("A variável de ambiente NEXT_PUBLIC_API_METRICS não está definida.");
    }

    const response = await fetch(apiUrl);
    
    if (!response.ok) {
      throw new Error(`Erro na requisição: ${response.status}`);
    }

    const data = await response.json();

    return NextResponse.json(data);
  } catch (error) {
    console.error(error);
    return NextResponse.json({ error: 'Erro ao obter dados da API externa' }, { status: 500 });
  }
}
