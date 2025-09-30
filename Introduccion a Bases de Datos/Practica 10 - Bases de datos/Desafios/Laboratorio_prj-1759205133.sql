CREATE TABLE IF NOT EXISTS "Cliente" (
	"id" serial NOT NULL UNIQUE,
	"Nombre" varchar(255) NOT NULL,
	"Apellido" varchar(255) NOT NULL,
	"Fecha_nacimiento" date NOT NULL,
	"Direccion" varchar(255) NOT NULL,
	"Localidad" bigint NOT NULL,
	"Telefono" varchar(255) NOT NULL,
	PRIMARY KEY ("id")
);

CREATE TABLE IF NOT EXISTS "Localidad" (
	"id" serial NOT NULL UNIQUE,
	"Nombre" varchar(255) NOT NULL,
	"CP" varchar(255) NOT NULL,
	"Provincia" bigint NOT NULL,
	PRIMARY KEY ("id")
);

CREATE TABLE IF NOT EXISTS "Movimiento" (
	"id" serial NOT NULL UNIQUE,
	"Letra" varchar(255) NOT NULL,
	"Fecha" date NOT NULL,
	"Cliente" bigint NOT NULL,
	PRIMARY KEY ("id")
);

CREATE TABLE IF NOT EXISTS "Provincia" (
	"id" serial NOT NULL UNIQUE,
	"Nombre" varchar(255) NOT NULL,
	"Pais" varchar(255) NOT NULL,
	PRIMARY KEY ("id")
);

CREATE TABLE IF NOT EXISTS "Item" (
	"id" serial NOT NULL UNIQUE,
	"Detalle" varchar(255) NOT NULL,
	"Cantidad" bigint NOT NULL,
	"Valor" numeric(10,0) NOT NULL,
	"Movimiento" bigint NOT NULL,
	PRIMARY KEY ("id")
);

ALTER TABLE "Cliente" ADD CONSTRAINT "Cliente_fk5" FOREIGN KEY ("Localidad") REFERENCES "Localidad"("id");
ALTER TABLE "Localidad" ADD CONSTRAINT "Localidad_fk3" FOREIGN KEY ("Provincia") REFERENCES "Provincia"("id");
ALTER TABLE "Movimiento" ADD CONSTRAINT "Movimiento_fk3" FOREIGN KEY ("Cliente") REFERENCES "Cliente"("id");

ALTER TABLE "Item" ADD CONSTRAINT "Item_fk4" FOREIGN KEY ("Movimiento") REFERENCES "Movimiento"("id");