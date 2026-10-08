# BITACORA PERSONAL — CLASE 10
# Tema: tránsito y calidad del aire en Montevideo (junio de 2024)
# Reconstrucción de práctica basada en los materiales de clase10.
# No es una transcripción de ejercicios obligatorios de la profesora.
# Para ejecutar: abrir el proyecto de la profesora como directorio de trabajo.

library(dplyr)
library(readr)
library(lubridate)
library(ggplot2)

# 1. Cargar la tabla de tránsito y calidad del aire
ruta <- "clases/clase10/transito_aire_junio2024.csv"
aire <- read_csv(ruta, show_col_types = FALSE)
glimpse(aire)
head(aire)

# 2. ¿Cuántos registros hay por estación?
aire |> count(estacion)

# 3. ¿Qué datos faltan por estación?
faltantes <- aire |>
  group_by(estacion) |>
  summarise(
    filas = n(),
    sin_transito = sum(is.na(transito)),
    sin_no2 = sum(is.na(no2)),
    sin_pm25 = sum(is.na(pm25)),
    .groups = "drop"
  )
print(faltantes)

# 4. ¿Cómo cambia el tránsito a lo largo del día?
datos <- aire |>
  mutate(h = hour(hora))
por_hora <- datos |>
  group_by(estacion, h) |>
  summarise(transito_promedio = mean(transito, na.rm = TRUE), .groups = "drop")

ggplot(por_hora, aes(x = h, y = transito_promedio)) +
  geom_line() +
  facet_wrap(~ estacion, scales = "free_y") +
  labs(title = "Tránsito promedio por hora", x = "Hora del día", y = "Vehículos por hora")

# 5. ¿Se relaciona el tránsito con la concentración de NO2?
correlaciones <- datos |>
  group_by(estacion) |>
  summarise(
    pares_validos = sum(complete.cases(transito, no2)),
    correlacion = if (sum(complete.cases(transito, no2)) >= 2)
      cor(transito, no2, use = "complete.obs") else NA_real_,
    .groups = "drop"
  )
print(correlaciones)

# 6. Graficar la relación para las estaciones que tienen NO2
datos |>
  filter(!is.na(no2)) |>
  ggplot(aes(x = transito, y = no2)) +
  geom_point(alpha = 0.3) +
  facet_wrap(~ estacion, scales = "free_x") +
  labs(title = "Tránsito y NO2", x = "Vehículos por hora", y = "NO2 (µg/m³)")

# REFLEXIÓN PARA LA BITÁCORA
# - Una correlación describe asociación, no demuestra causalidad.
# - Hay que mirar los faltantes antes de comparar estaciones.
# - Los conteos de tránsito no son directamente comparables entre estaciones
#   porque no tienen la misma cantidad de puntos de medición cercanos.
