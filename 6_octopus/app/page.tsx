import { Box } from "@mui/material";
import ChartPage from "./src/pages/chart";

export default function Home() {
  // Dados simulados (os dados reais seriam consumidos via API)

  return (
    <Box sx={{ padding: 3, height: "400px" }}>
      <ChartPage></ChartPage>
    </Box>
  );
}
