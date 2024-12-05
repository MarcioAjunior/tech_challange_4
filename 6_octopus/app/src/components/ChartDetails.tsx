import React from "react";
import { Box, Typography } from "@mui/material";

interface ChartDetailsProps {
  details: {
    totalSales: number;
    averageSales: number;
  };
}

const ChartDetails: React.FC<ChartDetailsProps> = ({ details }) => {
  return (
    <Box>
      <Typography variant="h6">Detalhes do Gráfico</Typography>
      <Typography>Total de Vendas: {details.totalSales}</Typography>
      <Typography>
        Média de Vendas: {details.averageSales.toFixed(2)}
      </Typography>
    </Box>
  );
};

export default ChartDetails;
