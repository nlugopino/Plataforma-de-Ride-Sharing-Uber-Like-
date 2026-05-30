ALTER TABLE servicios
ADD COLUMN metodo_pago VARCHAR;

ALTER TABLE servicios
ADD COLUMN tipo_comprobante VARCHAR;

CREATE TABLE ubicaciones_frecuentes (
    id SERIAL PRIMARY KEY,
    tipo VARCHAR(50),
    direccion VARCHAR(255),
    pasajero_id INTEGER REFERENCES pasajeros(id)
);

ALTER TABLE servicios
ADD COLUMN propina FLOAT DEFAULT 0;