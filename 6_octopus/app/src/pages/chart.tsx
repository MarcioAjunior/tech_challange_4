"use client";

import React, { useState, useEffect } from "react";
import { Box, Grid, Typography, CircularProgress, Paper } from "@mui/material";
import Chart from "../components/Chart";
import DateSelector from "../components/DateSelector";

const ChartPage: React.FC = () => {
  const [data, setData] = useState({
    historico: [],
    projecao: [],
  });

  type MetricsData = {
    mse: string;
    data_drift: {
      ks_statistic: string;
      p_value: string;
      drift_detected: boolean;
    };
    avg_time_inference: string | null;
  };

  const [metrics, setMetrics] = useState<MetricsData | null>({
        mse : ''
        ,data_drift : {
            ks_statistic : ''
            ,p_value : ''
            ,drift_detected : false
        }
        ,avg_time_inference : ''
    });
  const [selectedDate, setSelectedDate] = useState<Date | null>(new Date());
  const [loading, setLoading] = useState(false);
  let isFetching = false; // Evitar múltiplos fetches simultâneos

  useEffect(() => {
    const fetchMetrics = async () => {
      try {
        setLoading(true);

        const response = await fetch("/api/metrics");
        if (!response.ok) {
          throw new Error("Erro ao buscar métricas");
        }
        const data: MetricsData = await response.json();
        setMetrics(data);
      } catch (err) {
        console.error("Erro ao buscar métricas:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchMetrics();
  }, [selectedDate]);

  const fetchChartData = async (startDate: string) => {
    try {
      const response = await fetch("/api/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ date: startDate }),
      });

      if (!response.ok) {
        throw new Error("Erro ao buscar dados do endpoint");
      }

      const data = await response.json();
      return data;
    } catch (error) {
      console.error("Erro ao buscar chartData:", error);
      throw error;
    }
  };

  const fetchData = async (startDate: string) => {
    if (isFetching) return;
    isFetching = true;

    setLoading(true);
    try {
      const chartData = await fetchChartData(startDate);

      if (!chartData) {
        console.error("chartData é null ou undefined");
        return;
      }

      if (Array.isArray(chartData.result)) {
        setData({
          historico: chartData.result,
          projecao: [],
        });
      } else if (chartData.detail) {
        console.log(chartData.detail)
        alert(`Erro: Não é possível predizer uma data 7 dias maior que o valor de fechamento mais recente!`);
      } else {
        console.warn("Formato inesperado em chartData:", chartData);
      }
    } catch (error) {
      console.error("Erro ao buscar os dados:", error);
    } finally {
      setLoading(false);
      isFetching = false;
    }
  };

  useEffect(() => {
    if (selectedDate) {
      const formattedDate = selectedDate.toISOString().split("T")[0]; // Formata a data para "YYYY-MM-DD"
      fetchData(formattedDate);
    }
  }, [selectedDate]);

  return (
    <Box sx={{ p: 3, background: "#D3D3D3" }}>
      <Grid container spacing={3}>
        {/* Seção principal do gráfico */}
        <Grid item xs={12} md={7}>
          {loading ? <CircularProgress /> : <Chart data={data} />}
        </Grid>

        {/* Seção de métricas */}
        <Grid item xs={12} md={5}>
          <Typography variant="h6" mb={2}>
            Seleção de Data
          </Typography>
          <DateSelector value={selectedDate} onChange={setSelectedDate} />

          <Grid container spacing={2} mt={3}>
            {/* Container 1 */}
            <Grid item xs={12} sm={4}>
              <Paper
                sx={{
                  p: 2,
                  display: "flex",
                  flexDirection: "column",
                  alignItems: "center",
                }}
              >
                <Typography
                  variant="subtitle1"
                  gutterBottom
                  sx={{ fontWeight: "bold" }}
                >
                  MSE
                </Typography>
                {/* @ts-ignore */}
                <Typography variant="body2"  sx={{ fontSize: "0.75rem" }}>
                  {metrics?.mse ?? ""}
                </Typography>
              </Paper>
            </Grid>

            {/* Container 2 */}
            <Grid item xs={12} sm={4}>
              <Paper
                sx={{
                  p: 2,
                  display: "flex",
                  flexDirection: "column",
                  alignItems: "center",
                }}
              >
                <Typography
                  variant="subtitle1"
                  gutterBottom
                  sx={{ fontWeight: "bold" }}
                >
                  DATA DRIFT
                </Typography>
                <Typography variant="body2"  sx={{ fontSize: "0.75rem" }}>
                  {metrics?.data_drift.ks_statistic ?? ""}
                </Typography>
                <Typography variant="body2"  sx={{ fontSize: "0.75rem" }}>
                  {metrics?.data_drift.p_value ?? ""}
                </Typography>
                <Typography variant="body2"  sx={{ fontSize: "0.75rem" }}>
                  {metrics?.data_drift?.drift_detected
                    ? "Drift detectado"
                    : "Nenhum drift detectado"}
                </Typography>
              </Paper>
            </Grid>

            {/* Container 3 */}
            <Grid item xs={12} sm={4}>
              <Paper
                sx={{
                  p: 2,
                  display: "flex",
                  flexDirection: "column",
                  alignItems: "center",
                }}
              >
                <Typography
                  variant="subtitle1"
                  gutterBottom
                  textAlign={"center"}
                  sx={{ fontWeight: "bold" }}
                >
                  TEMPO MÉDIO DE INFERÊNCIA
                </Typography>
                <Typography variant="body2" >
                  {metrics?.avg_time_inference ?? ""}
                </Typography>
              </Paper>
            </Grid>
          </Grid>
        </Grid>
      </Grid>
    </Box>
  );
};

export default ChartPage;
