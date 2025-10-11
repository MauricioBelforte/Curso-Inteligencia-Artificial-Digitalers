



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