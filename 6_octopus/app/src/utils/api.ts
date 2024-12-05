export const fetchChartData = async (startDate: string) => {
  const historicoEProjecao = {
    historico: [
      {
        data: "2023-11-01",
        valor: 5.0,
        tipo: "1",
        descricao: "Valor do dólar na data",
      },
      {
        data: "2023-11-01",
        valor: 5.1,
        tipo: "2",
        descricao: "Valor do euro na data",
      },
      {
        data: "2023-11-02",
        valor: 5.2,
        tipo: "1",
        descricao: "Valor do dólar na data",
      },
      {
        data: "2023-11-02",
        valor: 5.3,
        tipo: "2",
        descricao: "Valor do euro na data",
      },
      {
        data: "2023-11-03",
        valor: 5.4,
        tipo: "1",
        descricao: "Valor do dólar na data",
      },
      {
        data: "2023-11-03",
        valor: 4.75,
        tipo: "2",
        descricao: "Valor do euro na data",
      },
      {
        data: "2023-11-04",
        valor: 7.0,
        tipo: "1",
        descricao: "Valor do dólar na data",
      },
      {
        data: "2023-11-04",
        valor: 6.0,
        tipo: "2",
        descricao: "Valor do euro na data",
      },
      {
        data: "2023-11-05",
        valor: 5.6,
        tipo: "1",
        descricao: "Conexão com a projeção",
      },
      {
        data: "2023-11-05",
        valor: 4.0,
        tipo: "2",
        descricao: "Conexão com a projeção",
      },
      {
        data: "2023-11-06",
        valor: 3.9,
        tipo: "2",
        descricao: "Conexão com a projeção",
      },
      {
        data: "2023-11-07",
        valor: 3.9,
        tipo: "2",
        descricao: "Conexão com a projeção",
      }   
    ]
  };

  return {
    historico: historicoEProjecao.historico,
  };
};
