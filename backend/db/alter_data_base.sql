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

ALTER TABLE servicios
ADD COLUMN tiene_objeto_perdido BOOLEAN DEFAULT FALSE;

CREATE TABLE objetos_perdidos (

    id SERIAL PRIMARY KEY,

    tipo VARCHAR(50),

    descripcion VARCHAR(255),

    fecha_reporte TIMESTAMP,

    servicio_id INTEGER UNIQUE REFERENCES servicios(id)
);