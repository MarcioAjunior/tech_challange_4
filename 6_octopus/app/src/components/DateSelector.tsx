"use client";

import React from "react";
import { LocalizationProvider } from "@mui/x-date-pickers";
import { AdapterDateFns } from "@mui/x-date-pickers/AdapterDateFns";
import { DatePicker } from "@mui/x-date-pickers/DatePicker";
import { TextField } from "@mui/material";

// Tipagem das props
interface DateSelectorProps {
  value: Date | null;
  onChange: (date: Date | null) => void;
}
const DateSelector: React.FC<DateSelectorProps> = ({ value, onChange }) => (
  <LocalizationProvider dateAdapter={AdapterDateFns}>
    <DatePicker
      label="Selecione uma Data"
      value={value}
      onChange={onChange}
      //@ts-ignore
      renderInput={(params) => <TextField {...params} />}
    />
  </LocalizationProvider>
);

export default DateSelector;
