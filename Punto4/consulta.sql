SELECT fecha, tipo_de_cambio
FROM cotizaciones c1
WHERE tipo_de_cambio = (
    SELECT MAX(tipo_de_cambio)
    FROM cotizaciones c2
    WHERE strftime('%Y-%m', c1.fecha) = strftime('%Y-%m', c2.fecha)
);