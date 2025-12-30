
SELECT 
  c.id_cliente,
  c.nombre,
  c.apellido,
  c.direccion,
  c.telefono,
  c.email,
  l."Nombre" AS Localidad, 
  l."Provincia"
FROM "Clientes" c
JOIN "Localidad" l ON c."localidadid" = l."LocalidadID"
ORDER BY c.id_cliente;



UPDATE "Clientes" SET 
  "nombre" = 'Juan',
  "apellido" = 'Pérez',
  "localidadid" = 1
WHERE "id_cliente" = 1;

UPDATE "Clientes" SET 
  "nombre" = 'María',
  "apellido" = 'Gómez',
  "localidadid" = 7
WHERE "id_cliente" = 2;

UPDATE "Clientes" SET 
  "nombre" = 'Carlos',
  "apellido" = 'Díaz',
  "localidadid" = 6
WHERE "id_cliente" = 3;

UPDATE "Clientes" SET 
  "nombre" = 'Laura',
  "apellido" = 'Fernández',
  "localidadid" = 2
WHERE "id_cliente" = 4;

UPDATE "Clientes" SET 
  "nombre" = 'Pedro',
  "apellido" = 'López',
  "localidadid" = 3
WHERE "id_cliente" = 5;

UPDATE "Clientes" SET 
  "nombre" = 'Ana',
  "apellido" = 'Torres',
  "localidadid" = 9
WHERE "id_cliente" = 6;

UPDATE "Clientes" SET 
  "nombre" = 'Luis',
  "apellido" = 'Martínez',
  "localidadid" = 8
WHERE "id_cliente" = 7;

UPDATE "Clientes" SET 
  "nombre" = 'Sofía',
  "apellido" = 'Castro',
  "localidadid" = 5
WHERE "id_cliente" = 8;

UPDATE "Clientes" SET 
  "nombre" = 'Martín',
  "apellido" = 'Ruiz',
  "localidadid" = 4
WHERE "id_cliente" = 9;

UPDATE "Clientes" SET 
  "nombre" = 'Paula',
  "apellido" = 'Herrera',
  "localidadid" = 10
WHERE "id_cliente" = 10;



INSERT INTO "Localidad" ("LocalidadID", "Nombre", "CP", "Provincia") VALUES
(1, 'Trelew', '9100', 'Chubut'),
(2, 'Rawson', '9103', 'Chubut'),
(3, 'Puerto Madryn', '9120', 'Chubut'),
(4, 'Comodoro Rivadavia', '9000', 'Chubut'),
(5, 'Esquel', '9200', 'Chubut'),
(6, 'Buenos Aires', '1000', 'Buenos Aires'),
(7, 'La Plata', '1900', 'Buenos Aires'),
(8, 'Rosario', '2000', 'Santa Fe'),
(9, 'Córdoba', '5000', 'Córdoba'),
(10, 'Mendoza', '5500', 'Mendoza');



ALTER TABLE "Clientes" ADD LocalidadID BIGINT;
ALTER TABLE "Clientes" ADD CONSTRAINT LocalidadID_fk4 FOREIGN KEY (localidadid) REFERENCES "Localidad"("LocalidadID");

/*
ALTER TABLE "Clientes" ALTER COLUMN "apellido" TYPE varchar(35);
ALTER TABLE "Clientes" ALTER COLUMN "apellido" SET NOT NULL;
*/

-- ALTER TABLE "Clientes" ADD COLUMN apellido varchar(200);

/*
ALTER TABLE "Clientes" ALTER COLUMN "nombre" TYPE varchar(30);
ALTER TABLE "Clientes" ALTER COLUMN "nombre" SET NOT NULL;
*/

--ALTER TABLE "Articulos" ALTER COLUMN "precio" SET NOT NULL;
-- ALTER TABLE "Articulos" ALTER COLUMN "nombre_articulo" TYPE varchar(75);



/*
CREATE TABLE IF NOT EXISTS "Localidad" (
	"LocalidadID" bigint NOT NULL, 
	"Nombre" varchar(40) NOT NULL, 
	"CP" varchar(10) NOT NULL, 
	"Provincia" varchar(20) NOT NULL,
	PRIMARY KEY ("LocalidadID")
);

*/

/*
INSERT INTO "Clientes" ("id_cliente", "nombre", "direccion", "telefono", "email") VALUES
(1, 'Juan Pérez', 'Av. Belgrano 123', '2804001000', 'juan.perez@mail.com'),
(2, 'María Gómez', 'Calle Rivadavia 450', '2804123456', 'maria.gomez@mail.com'),
(3, 'Carlos Díaz', 'San Martín 789', '2804556677', 'carlos.diaz@mail.com'),
(4, 'Laura Fernández', 'Mitre 222', '2804667788', 'laura.fernandez@mail.com'),
(5, 'Pedro López', 'Sarmiento 350', '2804778899', 'pedro.lopez@mail.com'),
(6, 'Ana Torres', 'Chacabuco 800', '2804889900', 'ana.torres@mail.com'),
(7, 'Luis Martínez', 'Moreno 1234', '2804990011', 'luis.martinez@mail.com'),
(8, 'Sofía Castro', '9 de Julio 555', '2804333222', 'sofia.castro@mail.com'),
(9, 'Martín Ruiz', 'Belgrano 333', '2804111222', 'martin.ruiz@mail.com'),
(10, 'Paula Herrera', 'Rawson 900', '2804222333', 'paula.herrera@mail.com');

INSERT INTO "Articulos" ("id_articulo", "nombre_articulo", "descripcion", "precio", "stock") VALUES
(1, 'Mouse inalámbrico', 'Mouse óptico Bluetooth', 5000, 25),
(2, 'Teclado mecánico', 'Teclado retroiluminado', 15000, 10),
(3, 'Monitor 24"', 'Full HD LED', 85000, 8),
(4, 'Auriculares', 'Auriculares con micrófono', 7000, 30),
(5, 'Pendrive 32GB', 'USB 3.0 Kingston', 4000, 50),
(6, 'Notebook', 'Core i5 8GB RAM 512GB SSD', 450000, 5),
(7, 'Cable HDMI', 'Cable 1.5 metros', 2500, 60),
(8, 'Parlantes', 'Parlantes estéreo 20W', 12000, 15),
(9, 'Webcam', 'HD 720p con micrófono', 18000, 12),
(10, 'Impresora', 'Multifunción WiFi Epson', 130000, 6);


INSERT INTO "Facturas" ("id_factura", "id_cliente", "fecha", "total", "estado") VALUES
(1, 1, '2025-10-01', 55000, 'Pagada'),
(2, 2, '2025-10-02', 9000, 'Pendiente'),
(3, 3, '2025-10-03', 150000, 'Pagada'),
(4, 4, '2025-10-04', 7000, 'Pagada'),
(5, 5, '2025-10-05', 130000, 'Pendiente'),
(6, 6, '2025-10-06', 4800, 'Pagada'),
(7, 7, '2025-10-07', 470000, 'Pagada'),
(8, 8, '2025-10-08', 21000, 'Pendiente'),
(9, 9, '2025-10-09', 87500, 'Pagada'),
(10, 10, '2025-10-10', 4000, 'Pagada');



INSERT INTO "DetalleFactura" ("id_detalle", "id_factura", "id_articulo", "cantidad", "precio_unitario") VALUES
(1, 1, 1, 2, 5000),
(2, 1, 2, 3, 15000),
(3, 2, 4, 1, 7000),
(4, 2, 7, 2, 2500),
(5, 3, 6, 1, 450000),
(6, 4, 4, 1, 7000),
(7, 5, 10, 1, 130000),
(8, 6, 5, 1, 4000),
(9, 7, 6, 1, 450000),
(10, 8, 8, 2, 12000);



*/


/* 
CREATE TABLE IF NOT EXISTS "Clientes" (
	"id_cliente" bigint NOT NULL,
	"nombre" varchar(255) NOT NULL,
	"direccion" varchar(255),
	"telefono" varchar(255),
	"email" varchar(255),
	PRIMARY KEY ("id_cliente")
);

CREATE TABLE IF NOT EXISTS "Articulos" (
	"id_articulo" bigint NOT NULL,
	"nombre_articulo" varchar(255) NOT NULL,
	"descripcion" varchar(255),
	"precio" numeric(10,0),
	"stock" bigint,
	PRIMARY KEY ("id_articulo")
);

CREATE TABLE IF NOT EXISTS "Facturas" (
	"id_factura" bigint NOT NULL,
	"id_cliente" bigint NOT NULL,
	"fecha" date,
	"total" numeric(10,0),
	"estado" varchar(255),
	PRIMARY KEY ("id_factura")
);

CREATE TABLE IF NOT EXISTS "DetalleFactura" (
	"precio_unitario" numeric(10,0),
	"id_detalle" bigint NOT NULL,
	"id_factura" bigint NOT NULL,
	"id_articulo" bigint NOT NULL,
	"cantidad" bigint,
	PRIMARY KEY ("id_detalle")
);



ALTER TABLE "Facturas" ADD CONSTRAINT "Facturas_fk1" FOREIGN KEY ("id_cliente") REFERENCES "Clientes"("id_cliente");
ALTER TABLE "DetalleFactura" ADD CONSTRAINT "DetalleFactura_fk2" FOREIGN KEY ("id_factura") REFERENCES "Facturas"("id_factura");

ALTER TABLE "DetalleFactura" ADD CONSTRAINT "DetalleFactura_fk3" FOREIGN KEY ("id_articulo") REFERENCES "Articulos"("id_articulo");

*/
