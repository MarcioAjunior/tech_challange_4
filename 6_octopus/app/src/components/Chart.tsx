// src/components/Chart.tsx

import React from "react";
import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

interface ChartProps {
  data: {
    historico: {
      data: string;
      valor: number;
      tipo: string;
      descricao: string;
    }[];
  };
}

const Chart: React.FC<ChartProps> = ({ data }) => {

    const usdHistorico = (data.historico ? data.historico.filter((item) => item.tipo === "1") : []);
    const eurHistorico = (data.historico ? data.historico.filter((item) => item.tipo === "2") : []);

    const usdLabels = [
    ...usdHistorico.map((item) => item.data)
  ].sort((a, b) => new Date(a).getTime() - new Date(b).getTime());

  const eurLabels = [
    ...eurHistorico.map((item) => item.data)
  ].sort((a, b) => new Date(a).getTime() - new Date(b).getTime());
  const labels = Array.from(new Set([...usdLabels, ...eurLabels]));

  const chartData = {
    labels,
    datasets: [
      {
        label: 'Valores fechados',
        data: labels.map(
          (label) =>
            usdHistorico.find((item) => item.data === label)?.valor || null
        ),
        borderColor: "green",
        tension: 0.1,

        backgroundColor: "rgba(0, 0, 255, 0.1)",
        fill: true,
      },
      {
        label: 'Valores previstos',
        data: labels.map(
          (label) =>
            eurHistorico.find((item) => item.data === label)?.valor || null
        ),
        borderColor: "orange",
        tension: 0.1,

        backgroundColor: "rgba(0, 255, 0, 0.1)",
        fill: true,
      }
    ],
  };

  const options = {
    responsive: true,
    scales: {
      x: { title: { display: true, text: "Data" } },
      y: { title: { display: true, text: "Valor" } },
    },
  };

  return <Line data={chartData} options={options} />;
};

export default Chart;
